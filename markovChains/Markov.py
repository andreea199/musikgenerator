import numpy as np


def make_pairs(fileArray):
    dict = []
    for i in range(len(fileArray) - 1):
        dict.append((fileArray[i], fileArray[i + 1]))
    return dict


def markov_chains(input, output):
    f = open(input).read()
    partituri = f.split(" ")

    pairs = make_pairs(partituri)
    dictionar = {}

    for word_1, word_2 in pairs:
        if word_1 in dictionar.keys():
            dictionar[word_1].append(word_2)
        else:
            dictionar[word_1] = [word_2]

    new = np.random.choice(partituri)

    with open(output, 'w') as out:
        for i in range(20):
            out.write(np.random.choice(dictionar[new[-1]])+"\n")
