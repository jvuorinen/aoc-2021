import numpy as np
from utils import read_input, array_to_string
import re


def get_cleaned_input():
    coords_raw, folds_raw = read_input("inputs/day_13.txt", "\n\n")

    coords = [tuple(map(int, x.split(","))) for x in coords_raw.split()]
    x_max, y_max = map(max, zip(*coords))
    arr = np.zeros(shape=(y_max + 1, x_max + 1)).astype(int)
    for x, y in coords:
        arr[y, x] = 1

    matches = re.findall(r"[x|y]=\d+", folds_raw)
    tmp = [tuple(x.split("=")) for x in matches]
    folds = [(a, int(b)) for a, b in tmp]

    return arr, folds


def fold(arr, axis, i):
    if axis == "y":
        old = arr[:i]
        new = np.flip(arr[i + 1 :], axis=0)

        diff = old.shape[0] - new.shape[0]
        if diff < 0:
            pad = np.zeros_like(arr)[: abs(diff), :]
            padded = np.vstack([pad, old])
            result = new + padded
        elif diff > 0:
            pad = np.zeros_like(old)[: abs(diff), :]
            padded = np.vstack([pad, new])
            result = old + padded
        else:
            result = old + new

    elif axis == "x":
        old = arr[:, :i]
        new = np.flip(arr[:, i + 1 :], axis=1)

        diff = old.shape[1] - new.shape[1]
        if diff < 0:
            pad = np.zeros_like(arr)[:, : abs(diff)]
            padded = np.hstack([pad, old])
            result = new + padded
        elif diff > 0:
            pad = np.zeros_like(arr)[:, : abs(diff)]
            padded = np.hstack([pad, new])
            result = old + padded
        else:
            result = old + new

    return result


def solve_1(arr, folds):
    axis, i = folds[0]

    folded = fold(arr, axis, i)
    result = (folded > 0).sum()

    return result


def solve_2(arr, folds):
    arr = arr.copy()

    for axis, i in folds:
        arr = fold(arr, axis, i)

    as_bin = (arr > 0).astype(int)
    s = array_to_string(as_bin, {0: " ", 1: "▓"})
    return s


if __name__ == "__main__":
    arr, folds = get_cleaned_input()

    answer_1 = solve_1(arr, folds)
    answer_2 = solve_2(arr, folds)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer:\n\n{answer_2}")
