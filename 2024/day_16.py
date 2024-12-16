from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm
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
        return p, d*(-1j)
    return p, d*1j


# def crawl(p, d, scr, seen):
#     # print(f"crawl {p, d}")
#     if p == end:
#         return

#     for m, s in MOVES.items():
#         _p, _d = apply(p, d, m)
#         _scr = scr + s
#         if M[_p] in '.SE' and _scr < seen.get((_p, _d), 9999999):
#             # print(f"update {_p, _d, scr} => {_p, _d, }")
#             seen[(_p,_d)] = _scr
#             crawl(_p, _d, _scr, seen)

ids = count(0)
# paths = []

def crawl(Q, seen):
    scr, _, p, d = heappop(Q)
    # print(f"crawl {p, d, scr}")
    if p == end:
        # paths.append(str(path))
        return
    
    for m, s in MOVES.items():
        _p, _d = apply(p, d, m)
        _scr = scr + s
        if M[_p] in '.SE' and _scr < seen.get((_p, _d), 9999999):
            # print(f"update {_p, _d, scr} => {_p, _d, }")
            seen[(_p,_d)] = _scr
            heappush(Q, (_scr, next(ids), _p, _d))

    crawl(Q, seen)


# raw = read().split("\n")
raw = read(2024, 16).split("\n")

M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}
start = next(k for k, v in M.items() if v == 'S')
end = next(k for k, v in M.items() if v == 'E')


seen = {(start, 1): 0}
Q = []
heappush(Q, (0, next(ids), start, 1))
crawl(Q, seen)



# len(set([p for (p, x) in M.items() if x in '.SE']))
# len(set([p for (p, d), v in seen.items()]))

# [(p, d, v) for (p, d), v in seen.items() if p == end]

# best = set()

# seen = {(start, 1): 0}
# crawl(start, 1, 0, seen, [])

a1 = min([v for (p,d), v in seen.items() if p == end])
a2 = None

print_answers(a1, a2, day=16)

