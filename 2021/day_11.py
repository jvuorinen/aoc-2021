import numpy as np

from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_11.txt")
    arr = np.array(list(map(list, raw_in))).astype(int)
    return arr


def clamp(n, bottom, top):
    return min(max(0, n), top)


def get_neighbor_idxs(i, j, arr):
    shape_i, shape_j = arr.shape

    i_low = clamp(i - 1, 0, shape_i - 1)
    i_hi = clamp(i + 1, 0, shape_i - 1)
    j_low = clamp(j - 1, 0, shape_j - 1)
    j_hi = clamp(j + 1, 0, shape_j - 1)

    return i_low, i_hi, j_low, j_hi


def step(previous):
    arr = previous + 1
    already_flashed = np.zeros_like(arr, dtype=bool)
    n_flashes = 0

    flashing = (arr > 9) & (~already_flashed)
    while flashing.sum() > 0:
        n_flashes += flashing.sum()

        for i, j in zip(*np.where(flashing)):
            already_flashed[i, j] = True
            i_low, i_hi, j_low, j_hi = get_neighbor_idxs(i, j, arr)
            arr[i_low : i_hi + 1, j_low : j_hi + 1] += 1

        flashing = (arr > 9) & (~already_flashed)
    arr[arr > 9] = 0
    return arr, n_flashes


def solve_1(arr):
    arr = arr.copy()
    total = 0

    for _ in range(100):
        arr, n_flahes = step(arr)
        total += n_flahes

    return total


def solve_2(arr):
    FAILSAFE = 10_000
    arr = arr.copy()

    for i in range(1, FAILSAFE):
        arr, n_flashes = step(arr)

        if n_flashes == 100:
            return i


if __name__ == "__main__":
    arr = get_cleaned_input()

    answer_1 = solve_1(arr)
    answer_2 = solve_2(arr)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
