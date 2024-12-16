from itertools import count
from collections import defaultdict
from heapq import heappush, heappop
import sys
from utils import read, print_answers

sys.setrecursionlimit(100_000)

MOVES = {
    "f": 1,
    "l": 1000,
    "r": 1000,
}


def apply(p, d, m):
    if m == "f":
        return p + d, d
    if m == "l":
        return p, d * (-1j)
    return p, d * 1j


def crawl(Q, seen):
    scr, _, p, d = heappop(Q)
    if p == end:
        return

    for m, s in MOVES.items():
        _p, _d = apply(p, d, m)
        _scr = scr + s
        if M[_p] in ".SE" and _scr <= seen.get((_p, _d), 9999999):
            predecessors[(_p, _d)].add((p, d))
        if M[_p] in ".SE" and _scr < seen.get((_p, _d), 9999999):
            seen[(_p, _d)] = _scr
            heappush(Q, (_scr, next(idgen), _p, _d))

    crawl(Q, seen)


def count_predecessors(n, prds):
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
crawl(Q, seen)

endnode = next((p, d) for (p, d), v in seen.items() if p == end)

a1 = seen[endnode]
a2 = count_predecessors(endnode, set())

print_answers(a1, a2, day=16)
