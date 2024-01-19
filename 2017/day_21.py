import numpy as np
from utils import read, print_answers

raw = read(2017, 21).split("\n")

rules = {}
for line in raw:
    fr, to = line.split(" => ")
    arr = np.array([list(x) for x in fr.split("/")]) == "#"
    to = np.array([list(x) for x in to.split("/")]) == "#"
    for _ in range(2):
        for _ in range(4):
            arr = np.rot90(arr)
            rules[tuple(map(tuple, arr))] = to
        arr = np.fliplr(arr)


def solve(n):
    arr = np.array([[False, True, False], [False, False, True], [True, True, True]])
    for _ in range(n):
        t = len(arr) // (3, 2)[len(arr) % 2 == 0]
        parts = [[rules[tuple(map(tuple, a))] for a in np.hsplit(a, t)] for a in np.vsplit(arr, t)]
        arr = np.vstack([*map(np.hstack, parts)])
    return arr.sum()


a1 = solve(5)
a2 = solve(18)
print_answers(a1, a2, day=21)  # 136 1911767
