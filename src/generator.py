from math import exp
from random import choices
from json import dumps


def generate(scale, length):
    full_scale = [scale[i % 12] for i in range(128)]
    note = choices(range(60, 72), weights=scale)[0]
    notes = [note]
    full_weights = []
    for i in range(length):
        weightf = lambda i, p: 15 * exp(-((i - p) ** 2) / (2 * 6 ** 2))
        prob = [weightf(j, note) for j in range(128)]
        weights = [round(full_scale[j] * prob[j]) for j in range(128)]

        notes.append(choices(range(128), weights=weights)[0])
        print(weights)
        full_weights.append(weights)
    print(notes)

    with open('data.json', 'w') as file:
        file.write(dumps({
            "weights": full_weights,
            "notes": notes
        }, indent=4))
    return notes
