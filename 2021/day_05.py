from functools import reduce
from collections import Counter

import numpy as np

from utils import read_input


def parse_line(line):
    x, y, x2, y2 = [int(x) for x in line.replace(" -> ", ",").split(",")]

    y_length = abs(y2 - y)
    x_length = abs(x2 - x)
    length = max(y_length, x_length)
    is_diagonal = x_length == y_length
    coords = []

    for _ in range(length + 1):
        coords.append((x, y))
        x += np.sign(x2 - x)
        y += np.sign(y2 - y)

    return coords, is_diagonal


def get_cleaned_input():
    raw_in = read_input("inputs/day_05.txt")
    tmp = [parse_line(line) for line in raw_in]

    diagonals = [coords for coords, is_diag in tmp if is_diag]
    straights = [coords for coords, is_diag in tmp if not is_diag]

    return diagonals, straights


def count_overlaps(coords):
    flat = reduce(list.__add__, coords)
    counter = Counter(flat)
    n = len([v for v in counter.values() if (v > 1)])
    return n


if __name__ == "__main__":
    diagonals, straights = get_cleaned_input()

    answer_1 = count_overlaps(straights)
    answer_2 = count_overlaps(diagonals + straights)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
