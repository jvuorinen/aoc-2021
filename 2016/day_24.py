from itertools import combinations, permutations, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
import re
import networkx as nx
from utils import read, print_answers


raw = read(2016, 24).split("\n")

M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}
floor = {k for k, v in M.items() if v != '#'}
nums = {v for v in M.values() if v.isdigit()}

def bfs(num):
    start = next(k for k, v in M.items() if v == num)
    todo = [(0, start)]
    ok = floor - {start}
    res = {}
    while todo:
        i, n = todo.pop(0)
        if i > 0 and (k := M.get(n, "")).isnumeric():
            res[k] = i
        for nn in (n+1, n-1, n+1j, n-1j):
            if nn in ok:
                ok.remove(nn)
                todo.append((i+1, nn))
    return res

D = {n: bfs(n) for n in nums}
D

a1 = None
a2 = None

print_answers(a1, a2, day=24)
