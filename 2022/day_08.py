from utils import read_file, print_answers
import numpy as np
from itertools import product

cummax = np.maximum.accumulate

if __name__ == "__main__":
    raw_in = read_file("inputs/day_08b.txt").split()
    arr = np.array([list(x) for x in raw_in], dtype=int)

    # Part 1
    wiz = lambda arr: arr > cummax(np.pad(arr + 1, (1, 0))[:-1, 1:] - 1)
    a1 = np.add.reduce([np.rot90(wiz(np.rot90(arr, k)), -k) for k in range(4)], dtype=bool).sum()

    # Part 2
    poof = lambda s, x: np.sum(x > cummax(np.pad(s, (1, 0))[:-1]))
    zap = lambda arr, i, j: (
        arr[i, (j + 1) :],
        arr[i, :j][::-1],
        arr[(i + 1) :, j],
        arr[:i, j][::-1],
    )
    swish = lambda i, j: np.prod([poof(x, arr[i, j]) for x in zap(arr, i, j)])
    a2 = max([swish(*x) for x in product(*map(range, arr.shape))])

    print_answers(a1, a2, day=8)
