from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm
from utils import read, print_answers

# raw = read().split("\n")
raw = read(2024, 20).split("\n")
M = {c + 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}


def get_next(i, x, n, d):
    nxt = []
    for j in (1, 1j, -1j):
        if M.get(nn := (n + j*d), 'x') in '.E':
            nxt.append((i+1, x, nn, j*d))
        if x and M.get(nn := (n + 2*j*d), 'x') in '.E':
            nxt.append((i+2, x-1, nn, j*d))
    return nxt


# def bfs(x):
#     n = next(k for k, v in M.items() if v == 'S')
#     d = next(d for d in (1, -1, -1j, 1j) if M.get(n+d) == '.')
#     end = next(k for k, v in M.items() if v == 'E')

#     best = {}
#     todo = [(0, x, n, d)]
#     res = []
#     while todo:
#         # print(todo)
#         i, x, n, d = todo.pop(0)
#         if n == end:
#             res.append(i)
#         else:
#             for nxt in get_next(i, x, n, d):
#                 ii, xx, nn, dd = nxt
#                 if nn != end and best.get(nn, (0, 1e9)) > (-xx, ii):
#                     todo.append(nxt)
#                     best[nn] = (-xx, ii)
#     return res

start = next(k for k, v in M.items() if v == 'S')
end = next(k for k, v in M.items() if v == 'E')
floor = set([k for k, v in M.items() if v != '#'])
walls = set([k for k, v in M.items() if v == '#'])

def bfs(floor):
    floor = floor.copy()
    todo = [(0, start)]
    while todo:
        i, n = todo.pop(0)
        floor -= {n}
        if n == end:
            return i
        todo += [(i+1, nn) for d in (1, -1, 1j, -1j) if (nn := n+d) in floor]

ref = bfs(floor)

res = [bfs(floor | {w}) for w in tqdm(walls)]

a1 = len([x for x in res if ref - x >= 100])

a2 = None

print_answers(a1, a2, day=20)
