from itertools import permutations
from utils import read, print_answers

raw = read(2024, 12).split("\n")
M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}

# Get regions via flood fill
regions = []
while M:
    z, c = M.popitem()
    rg = set()
    todo = {z}
    while todo:
        z = todo.pop()
        rg.add(z)
        for n in set(_z for d in [1, -1, 1j, -1j] if (M.get(_z := z + d) == c) and _z not in rg):
            todo.add(n)
            M.pop(n)
    regions.append(rg)

# Calculations
a1 = a2 = 0
for rg in regions:
    adj = [p for p in permutations(rg, 2) if abs(p[0] - p[1]) == 1]
    perim = 4 * len(rg) - 2 * (len(adj) // 2)
    a1 += len(rg) * perim

    corr = sum(1 for a, b in adj if not rg & {a + (1j * (a - b)), b + (1j * (a - b))})
    a2 += len(rg) * (perim - corr)

print_answers(a1, a2, day=12)
