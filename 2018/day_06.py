import numpy as np
from utils import print_answers, read

SIZE = 400
PART_2_THRS = 10_000

raw_in = read("inputs/day_06b.txt").split("\n")
points = [complex(*map(int, p.split(","))) for p in raw_in]
arr = np.arange(SIZE)[:, None] + 1j * np.arange(SIZE)


def mdist(arr, c):
    return abs((arr - c).real) + abs((arr - c).imag)


dists = np.stack([mdist(arr, c) for c in points], axis=2)
closest = dists.argmin(axis=2)

# Find ties and infinites
mins = dists.min(axis=2).reshape((SIZE, SIZE, 1))
ties = (dists == mins).sum(axis=2) > 1

border = set(np.unique(closest[:, [0, -1]])) | set(np.unique(closest[[0, -1], :]))
infinites = np.isin(closest, list(border))

# ...and count them out
closest[ties | infinites] = -1

a1 = max([(closest == i).sum() for i in range(len(points))])
a2 = (dists.sum(axis=2) < PART_2_THRS).sum()
print_answers(a1, a2, day=6)
