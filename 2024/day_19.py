from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import finditer, findall
import networkx as nx
from tqdm import tqdm
from utils import read, print_answers

# raw = read()
raw = read(2024, 19)

a, b = raw.split('\n\n')
pats = a.split(', ')
mats = b.split('\n')

@cache
def matches(mat, s=0):
    # print(mat)
    if len(mat) == 0:
        return 1
    ps = set(pats)
    while ps:
        pgs = "|".join(f"{p}" for p in ps)
        p = f"^({pgs})(.*)$"
        if (match := findall(p, mat)):
            a, b = match[0]
            ps.remove(a)
            s += matches(b)
        else:
            break
        # print(match)
    return s

ns = [matches(m) for m in tqdm(mats)]

a1 = sum(x > 0 for x in ns)
a2 = sum(ns)

print_answers(a1, a2, day=19)
# 315
# 625108891232249