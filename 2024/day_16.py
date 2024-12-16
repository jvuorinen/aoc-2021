from itertools import count
from collections import defaultdict
from heapq import heappush, heappop
from utils import read, print_answers


def step(p, d, scr, move):
    if move == "f":
        return p + d, d, scr + 1
    return p, d * (1j, -1j)[move == "r"], scr + 1000


def count_predecessors(n, prds=None):
    prds = prds or set()
    prds.add(n[0])
    for nn in predecessors[n]:
        count_predecessors(nn, prds)
    return len(prds)


raw = read(2024, 16).split("\n")

M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}
start = next(k for k, v in M.items() if v == "S")
end = next(k for k, v in M.items() if v == "E")

idgen = count(0)
predecessors = defaultdict(set)
seen = {(start, 1): 0}
Q = [(0, next(idgen), start, 1)]
while True:
    scr, _, p, d = heappop(Q)
    if p == end:
        break
    for move in "flr":
        _p, _d, _scr = step(p, d, scr, move)
        best = seen.get((_p, _d), float("inf"))
        if M[_p] in ".SE":
            if _scr <= best:
                predecessors[(_p, _d)].add((p, d))
            if _scr < best:
                seen[(_p, _d)] = _scr
                heappush(Q, (_scr, next(idgen), _p, _d))

endnode = next((p, d) for (p, d), _ in seen.items() if p == end)

a1 = seen[endnode]
a2 = count_predecessors(endnode)

print_answers(a1, a2, day=16)
