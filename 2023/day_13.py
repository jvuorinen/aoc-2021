import numpy as np
from utils import read_file, print_answers


def find_split(arr, smudges):
    for i in range(1, arr.shape[0]):
        a = arr[i:]
        b = np.flip(arr[:i], 0)
        if sum([sum(a != b) for a, b in zip(a, b)]) == smudges:
            return i
    return 0


def count_arr(arr, smudges):
    return 100 * find_split(arr, smudges) + find_split(arr.T, smudges)


raw = read_file("inputs/day_13b.txt").split("\n\n")
arrs = [np.array([list(r) for r in x.split("\n")]) for x in raw]

a1 = sum([count_arr(arr, smudges=0) for arr in arrs])
a2 = sum([count_arr(arr, smudges=1) for arr in arrs])

print_answers(a1, a2, day=13)  # Correct: 34202, 34230
