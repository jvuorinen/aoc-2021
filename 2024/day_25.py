from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm
from utils import read, print_answers

# raw = read().split("\n\n")
raw = read(2024, 25).split("\n\n")

keys = []
locks = []
for r in raw:
    arr = np.array([list(x) for x in r.split("\n")])
    arr = np.rot90(arr)
    if arr[0,0] == "#":
        keys.append((arr == "#").astype(int))
    else:
        locks.append((arr == "#").astype(int))

a1 = 0
for k, l in product(keys, locks):
    s = k.shape
    # print(k+l)
    # print(((k+l) > 1).sum(), (k,l))
    a1 += ((k+l) > 1).sum() == 0

# a1 = None
a2 = None

print_answers(a1, a2, day=25)
