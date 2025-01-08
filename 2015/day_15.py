from itertools import permutations, combinations_with_replacement as cwr
import numpy as np
import re
from utils import read, print_answers

raw = read(2015, 15).split("\n")
ingredients = np.array([[*map(int, re.findall(r"-?\d+", x))] for x in raw])
recipes = np.vstack([[*permutations(c)] for c in cwr(range(101), 4) if sum(c) == 100])

M = (recipes @ ingredients).clip(0)
scores = M[:, :-1].prod(axis=1)
cal500 = M[:, -1] == 500
print_answers(scores.max(), scores[cal500].max(), day=15)
