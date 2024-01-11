import numpy as np
from utils import read_file, print_answers, get_neighbors


arr = np.array([list(x) for x in read_file("inputs/day_03.txt").split("\n")])

symbol_locs = set(zip(*np.where(~np.isin(arr, list("1234567890.")))))
symbols = {loc: arr[loc] for loc in symbol_locs}

groups = {loc: [] for loc in symbol_locs}
num = ""
neighbors = set()
for (i, j), x in np.ndenumerate(arr):
    if x in "1234567890":
        num += x
        neighbors |= set(get_neighbors((i, j), diag=True))
    elif num or (j == arr.shape[1] - 1):
        if sloc := (symbol_locs & neighbors):
            groups[sloc.pop()].append(int(num))
        num = ""
        neighbors = set()

a1 = sum([sum(v) for v in groups.values()])
a2 = sum([v[0] * v[1] for k, v in groups.items() if (symbols.get(k) == "*" and len(v) == 2)])

print_answers(a1, a2, day=3)  # Correct: 539433, 75847567
