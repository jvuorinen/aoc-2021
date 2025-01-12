from itertools import combinations
import numpy as np
import re
from utils import read, print_answers

BOSS = [*map(int, re.findall(r"\d+", read(2015, 21)))]

WPN = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
ARM = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
RINGS = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [60, 0, 3]]

win, lose = [], []
for wpn in WPN:
    for arm in [None] + ARM:
        for r1, r2 in combinations([None, None] + RINGS, 2):
            stats = np.array([0, 0, 0]) + wpn
            stats += arm or (0, 0, 0)
            stats += r1 or (0, 0, 0)
            stats += r2 or (0, 0, 0)

            t1 = BOSS[0] // max(1, stats[1] - BOSS[2])
            t2 = 100 // max(1, BOSS[1] - stats[2])
            ((lose, win)[t1 <= t2]).append(stats[0])

print_answers(min(win), max(lose), day=21)
