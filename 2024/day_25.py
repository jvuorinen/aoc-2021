from itertools import product
import numpy as np
from utils import read, print_answers

raw = read(2024, 25).split("\n\n")
arrs = [np.array([*map(list, r.split("\n"))]) for r in raw]
keys = [(a=="#").astype(int) for a in arrs if a[0][0] == "#"]
locks = [(a=="#").astype(int) for a in arrs if a[0][0] == "."]

a1 = sum(~np.any((k+l) > 1) for k, l in product(keys, locks))
print_answers(a1, None, day=25)
