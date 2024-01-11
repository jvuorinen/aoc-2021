from itertools import combinations
from utils import read, print_answers

a1 = a2 = 0
for line in read(2017, 2).split("\n"):
    ns = sorted([*map(int, line.split("\t"))])
    a1 += ns[-1] - ns[0]
    for a, b in combinations(ns, 2):
        if b % a == 0:
            a2 += b // a

print_answers(a1, a2, day=2)  # 41887 226
