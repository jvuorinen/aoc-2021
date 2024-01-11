import numpy as np
from utils import read_file, print_answers


def get_value(seq):
    diffs = [seq]
    while sum(abs(diffs[-1])) != 0:
        diffs.append(np.diff(diffs[-1]))
    return sum([x[-1] for x in diffs[::-1]])


raw_in = read_file("inputs/day_09b.txt").split("\n")
seqs = [np.array([int(x) for x in line.split()]) for line in raw_in]

a1 = sum([get_value(s) for s in seqs])
a2 = sum([get_value(s[::-1]) for s in seqs])

print_answers(a1, a2, day=9)  # Correct: 1882395907, 1005
