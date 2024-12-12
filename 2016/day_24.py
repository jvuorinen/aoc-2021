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

nums = {v: k for k, v in M.items() if v.isdigit()}
floor = {k for k, v in M.items() if v != '#'}

paths = defaultdict(dict)
for c in nums:
    i = 0
    seen = set()
    todo = {nums[c]}
    while todo:
        _todo = set()
        for z in todo:
            seen.add(z)
            if (cc := M[z]) != '.':
                paths[c][cc] = i
            ns = set([n for d in [1, -1, 1j, -1j] if (n := z + d) in floor and n not in seen])
            _todo |= ns
        i += 1
        todo = _todo

paths

a1 = max(paths['0'].values())
a2 = None

print_answers(a1, a2, day=24)
