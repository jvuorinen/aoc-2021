from itertools import count
from collections import defaultdict
from heapq import heappush, heappop
from utils import read, print_answers


def step(p, d, scr, move):
    if move == "f":
        return p + d, d, scr + 1
    return p, d * (1j, -1j)[move == "r"], scr + 1000


def count_predecessors(n, predecessors, res=None):
    res = res or set()
    res.add(n[0])
    for nn in predecessors[n]:
        count_predecessors(nn, predecessors, res)
    return len(res)


def dijkstra(start, end):
    p = start
    idgen = count(0)
    predecessors = defaultdict(set)
    D = {(p, 1): 0}
    Q = [(0, next(idgen), p, 1)]

    while p != end:
        scr, _, p, d = heappop(Q)
        for move in "flr":
            _p, _d, _scr = step(p, d, scr, move)
            best = D.get((_p, _d), float("inf"))
            if M[_p] in ".SE":
                if _scr <= best:
                    predecessors[(_p, _d)].add((p, d))
                if _scr < best:
                    D[(_p, _d)] = _scr
                    heappush(Q, (_scr, next(idgen), _p, _d))

    endnode = next((p, d) for (p, d), _ in D.items() if p == end)
    return D[endnode], count_predecessors(endnode, predecessors)


raw = read(2024, 16).split("\n")

M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}
start = next(k for k, v in M.items() if v == "S")
end = next(k for k, v in M.items() if v == "E")

a1, a2 = dijkstra(start, end)

print_answers(a1, a2, day=16)
