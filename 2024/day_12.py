from itertools import combinations, permutations
from utils import read, print_answers

raw = read(2024, 12).split("\n")

M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}

regions = []
while M:
    z, c = M.popitem()
    reg = set()
    todo = {z}
    while todo:
        z = todo.pop()
        reg.add(z)
        ns = set(_z for d in [1, -1, 1j, -1j] if (M.get(_z := z + d) == c) and _z not in reg)
        for n in ns:
            todo.add(n)
            M.pop(n)
    regions.append(reg)

a1 = a2 = 0
for reg in regions:
    adj = [p for p in combinations(reg, 2) if abs(p[0] - p[1]) == 1]
    perim = 4 * len(reg) - 2 * len(adj)
    a1 += len(reg) * perim

    corr = sum(
        1
        for a, b in permutations(reg, 2)
        if abs(d := a - b) == 1 and (a + (1j * d) not in reg) and (b + (1j * d) not in reg)
    )
    a2 += len(reg) * (perim - corr)

print_answers(a1, a2, day=12)
