from midiutil import MIDIFile
from random import choices, randint


def check(v: float, k: list[float], a: list[float]):
    if len(k) != len(a):
        raise ValueError(f'list {k} does not have the same length as list {a}')
    if not (v in k):
        raise ValueError(f'value {v} does not exist in list {k}')

    return a[k.index(v)]


def to_midi(notes):
    time = 0
    ti = [2, 3/2, 1, 3/4, 1/2, 3/8, 1/4]
    timeinterval = choices(ti)[0]
    velocity = 63
    gen = MIDIFile(1)
    gen.addTempo(0, 0, 120)

    for pitch in notes:
        half_note_weight = check(timeinterval, ti, [1, 1/4, 2, 1/16, 1/8, 1/16, 1/16])
        dot_quart_weight = check(timeinterval, ti, [1, 1, 1/2, 1/4, 2, 1/6, 1/12])
        quar_note_weight = check(timeinterval, ti, [1, 1/2, 2, 1/4, 1, 1/6, 1/8])
        dot_eight_weight = check(timeinterval, ti, [1, 1/3, 1, 1/2, 1, 1/2, 2])
        eigh_note_weight = check(timeinterval, ti, [1, 3, 1, 1/2, 2, 1/2, 1])
        dot_sixtn_weight = 1/3000
        sixt_note_weight = check(timeinterval, ti, [1, 1, 2, 5, 1, 1, 4])

        timeweights = [half_note_weight, dot_quart_weight, quar_note_weight, dot_eight_weight, eigh_note_weight,
                       dot_sixtn_weight, sixt_note_weight]
        timeinterval = choices(ti, weights=timeweights)[0]

        gen.addNote(0, 0, pitch, time, timeinterval, velocity)
        time += timeinterval
        velocity += randint(-5, 5)

    with open('generated.mid', 'wb') as file:
        gen.writeFile(file)
