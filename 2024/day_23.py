from itertools import combinations
from utils import read, print_answers


raw = read(2024, 23).split("\n")

con = set()
nodes = set()
for line in raw:
    a, b = line.split("-")
    nodes |= {a, b}
    con.add((a, b))
    con.add((b, a))


def all_connected(nds):
    if any((a, b) not in con for a, b in combinations(nds, 2)):
        return False
    return True


tn = {n for n in nodes if n.startswith("t")}
relevant = tn | {n for x in tn for n in nodes if (n, x) in con}
a1 = len([c for c in combinations(relevant, 3) if tn & set(c) and all_connected(c)])

a2 = None
groups = {frozenset({n} | {nn for nn in nodes if (n, nn) in con}) for n in nodes}
while not a2:
    allcon = [g for g in groups if all_connected(g)]
    if allcon:
        a2 = ",".join(sorted(allcon[0]))
    groups = {frozenset(a & b) for a, b in combinations(groups, 2)}
    maxsize = max(map(len, groups))
    groups = {g for g in groups if len(g) == maxsize}


print_answers(a1, a2, day=23)
