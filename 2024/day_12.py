from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm
from utils import read, print_answers

raw = read().split("\n")
# raw = read(2024, 12).split("\n")

M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}


regions = []

todo = set(M)
while todo:
    z = todo.pop()
    c = M.pop(z)
    
    r = set()
    buf = [z]
    while buf:
        z = buf.pop()
        r.add(z)
        ns = [nz for d in [1, -1, 1j, -1j] if M.get(nz  := z + d) == c and nz not in r]
        todo -= set(ns)
        buf += ns
    regions.append(r)


a1 = a2 = 0
for r in regions:
    adj = len([p for p in combinations(r, 2) if abs(p[0] - p[1]) == 1])
    perim = 4 * len(r) - 2 * adj
    a1 += len(r) * perim


print_answers(a1, a2, day=12)
# 634220788 high