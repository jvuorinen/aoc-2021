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
# raw = '2333133121414131402'
# raw = '45252'
raw = read(2024, 9)

files = [int(c)*[i] for i, c in enumerate(raw[::2])]
# files = "".join(files)

space = [int(c)*[None] for i, c in enumerate(raw[1::2])]
# space = ''.join(space)


# Part 1
data = reduce(list.__add__, [*chain(*zip(files, space + [[None]]))])

i = 0
while i < len(data)-1:
    while data[-1] is None:
        data.pop(-1)
    if data[i] is None:
        data[i] = data.pop(-1)
    i += 1
while data[-1] is None:
    data.pop(-1)

a1 = sum(i*x for i, x in enumerate(data))


# Part 2
data = reduce(list.__add__, [*chain(*zip(files, space + [[None]]))])

ixs = [data.index(i) for i in range(len(files))]
# data = np.array([-1 if x is None else x for x in data])

for i in reversed(range(len(files))):
    # print(i, ixs[i], files[i])
    # print()
    # print(f"attempting {i}")
    # print(data)
    s = len(files[i])
    io = ixs[i]
    for ii in range(io):
        if all(x is None for x in data[ii:ii+s]):
            data[ii:ii+s] = files[i]
            data[io:io+s] = [None] * s
            # print("moved")
            # print(data)
            break

a2 = sum(i*(x or 0) for i, x in enumerate(data))

print_answers(a1, a2, day=9)
# 6430446922192
# 6460170593016