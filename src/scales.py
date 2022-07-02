"""
ARRAYS FOR DIFFERENT SCALES
notes:
C  / B#  / Dbb :  0
C# / Db        :  1
D  / C## / Ebb :  2
D# / Eb        :  3
E  / Fb  / D## :  4
F  / Gbb / E#  :  5
F# / Gb        :  6
G  / F## / Abb :  7
G# / Ab        :  8
A  / G## / Bbb :  9
A# / Bb        : 10
B  / Cb        : 11
"""

IN = 1  # Chance of a note in the scale
OUT = 1/8  # Chance of a note outside the scale
OCTAVE = 2  # Chance of a unison / octave
FIFTH = 2.75  # Chance of a fifth
FOURTH = 2.5  # Chance of a fourth


def ts(rs: list[int]):
    out = [OUT for i in range(0, 12)]
    for i in rs:
        out[i % 11] = IN * (OCTAVE if i % 11 is rs[0] else FIFTH if i % 11 is rs[4] else FOURTH if i % 11 is rs[3] else 1)
    return out


# MAJOR SCALES
CN_MAJ = ts([0, 2, 4, 5, 7, 9, 11])
CS_MAJ = ts([1, 3, 5, 6, 8, 10, 12])
DN_MAJ = ts([2, 4, 6, 7, 9, 11, 13])
DS_MAJ = ts([3, 5, 7, 8, 10, 12, 14])
EN_MAJ = ts([4, 6, 8, 9, 11, 13, 15])
FN_MAJ = ts([5, 7, 9, 10, 12, 14, 16])
FS_MAJ = ts([6, 8, 10, 11, 13, 15, 17])
GN_MAJ = ts([7, 9, 11, 12, 14, 16, 18])
GS_MAJ = ts([8, 10, 12, 13, 15, 17, 19])
AN_MAJ = ts([9, 11, 13, 14, 16, 18, 20])
AS_MAJ = ts([10, 12, 14, 15, 17, 19, 21])
BN_MAJ = ts([11, 13, 15, 16, 18, 20, 22])

# MINOR SCALES
CN_MIN = ts([0, 2, 3, 5, 7, 8, 10])
CS_MIN = ts([1, 3, 4, 6, 8, 9, 11])
DN_MIN = ts([2, 4, 5, 7, 9, 10, 12])
DS_MIN = ts([3, 5, 6, 8, 10, 11, 13])
EN_MIN = ts([4, 6, 7, 9, 11, 12, 14])
FN_MIN = ts([5, 7, 8, 10, 12, 13, 15])
FS_MIN = ts([6, 8, 9, 11, 13, 14, 16])
GN_MIN = ts([7, 9, 10, 12, 14, 15, 17])
GS_MIN = ts([8, 10, 11, 13, 15, 16, 18])
AN_MIN = ts([9, 11, 12, 14, 16, 17, 19])
AS_MIN = ts([10, 12, 13, 15, 17, 18, 20])
BN_MIN = ts([11, 13, 14, 16, 18, 19, 21])
