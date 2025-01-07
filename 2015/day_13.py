from itertools import permutations
from collections import defaultdict
from utils import read, print_answers

H = defaultdict(int)
for line in read(2015, 13).split("\n"):
    a, _, op, n, *_, b = line[:-1].split(" ")
    H[a, b] = (-1, 1)[op == "gain"] * int(n)

names = list(set.union(*map(set, H)))


def score(prm):
    circle = list(prm) + [prm[0]]
    return sum(H[p] + H[p[::-1]] for p in zip(circle[:-1], circle[1:]))


a1 = max(map(score, permutations(names)))
a2 = max(map(score, permutations(names + ["me"])))

print_answers(a1, a2, day=13)
