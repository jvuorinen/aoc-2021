from itertools import combinations
from collections import defaultdict
from utils import read, print_answers

raw = read(2024, 8).split("\n")
A = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}

antennas = defaultdict(set)
for loc, x in A.items():
    if x != ".":
        antennas[x] |= {loc}

part1 = set()
part2 = set()
for tp, locs in antennas.items():
    for a1, a2 in combinations(locs, 2):
        d = a2 - a1
        part1 |= {a1 - d, a2 + d} & A.keys()
        part2 |= {a1}
        for dd in (d, -d):
            n = a1
            while (n := n + dd) in A:
                part2 |= {n}

print_answers(len(part1), len(part2), day=8)
