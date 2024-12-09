from itertools import combinations, permutations, product, count, cycle, chain
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm
from utils import read, print_answers

# raw = '12345'
raw = '2333133121414131402'
# raw = '45252'
# raw = read(2024, 9)

files = [int(c)*[i] for i, c in enumerate(raw[::2])]
space = [int(c)*[None] for i, c in enumerate(raw[1::2])]

original = reduce(list.__add__, [*chain(*zip(files, space + [[None]]))])

# Part 1

data = original.copy()

i, ii = 0, len(data) - 1
while True:
    while data[i] is not None:
        i += 1
    while data[ii] is None:
        ii -= 1
    if ii <= i:
        break
    data[i], data[ii] = data[ii], data[i]

a1 = sum(i*(x or 0) for i, x in enumerate(data))


# Part 2
data = original.copy()
ixs = [data.index(i) for i in range(len(files))]
# data = np.array([-1 if x is None else x for x in data])

for ii, f in zip(ixs[::-1], files[::-1]):
    s = len(f)
    for i in range(ii):
        if all(x is None for x in data[i:i+s]):
            data[i:i+s] = f
            data[ii:ii+s] = [None] * s
            break

a2 = sum(i*(x or 0) for i, x in enumerate(data))


print_answers(a1, a2, day=9)
# 6430446922192
# 6460170593016