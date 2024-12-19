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

def get_pattern(ps):
    pgs = "|".join(f"{p}" for p in ps)
    return f"^({pgs})(.*)$"


@cache
def matches(mat, s=0):
    if len(mat) == 0:
        return 1
    ps = set(pats)
    while (match := findall(get_pattern(ps), mat)):
        a, b = match[0]
        ps.remove(a)
        s += matches(b)
    return s

nways = [matches(m) for m in tqdm(mats)]

a1 = sum(x > 0 for x in nways)
a2 = sum(nways)

print_answers(a1, a2, day=19)
# 315
# 625108891232249