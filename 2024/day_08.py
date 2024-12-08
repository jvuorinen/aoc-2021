from itertools import combinations
from collections import defaultdict
from utils import read, print_answers

raw = read(2024, 8).split("\n")

ants = defaultdict(set)
space = set()

for r, line in enumerate(raw):
    for c, x in enumerate(line):
        if x != ".":
            ants[x] |= {c - 1j * r}
        space.add(c - 1j * r)

alt = set()
for tp, locs in ants.items():
    for a1, a2 in combinations(locs, 2):
        d = a2-a1
        new = a1
        while (new := new - d) in space:
            alt |= {new}
        new = a1    
        while (new := new + d) in space:
            alt |= {new}
        alt |= {a1}
        
a1 = len(alt)
a2 = None

print_answers(a1, a2, day=8)
