from itertools import product
import numpy as np
from utils import read, print_answers

def step(n):
    n = ((n*64) ^ n ) % m
    n = ((n//32) ^ n ) % m
    return ((n * 2048) ^ n)  % m

# for line in read().split("\n"):



raw = read().split("\n")
# raw = read(2024, 22).split("\n")
ns = np.array([*map(int, raw)])

m = 16777216


res = []
res.append(ns % 10)
for _ in range(2000):
    ns = np.array([*map(step, ns)])
    res.append(ns % 10)

p = np.array(res).T
d = np.diff(p)


pats = np.array([[row[i:i+4] for i in range(len(row)-3)] for row in d])
ds = [{} for _ in range(len(p))]
for i, m in enumerate(pats):
    for j, _p in enumerate(m[::-1], 1):
        ds[i][tuple(_p)] = p[i, -j]


def check_pattern(pat):
    return sum(d.get(pat, 0) for d in ds)
    


a1 = sum(ns)
a2 = max(check_pattern(p) for p in product(range(-10, 10), repeat=4))

print_answers(a1, a2, day=22)
# 1931
