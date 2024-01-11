from operator import mul
from functools import reduce
from itertools import product

import numpy as np

from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_09.txt")
    arr = np.array([list(map(int, list(line))) for line in raw_in])
    return arr


def add_coords(c1, c2):
    c = (c1[0] + c2[0], c1[1] + c2[1])
    return c


def is_within_bounds(coord, arr):
    dim_i, dim_j = arr.shape
    is_valid = (0 <= coord[0] < dim_i) & (0 <= coord[1] < dim_j)
    return is_valid


def get_neighbor_coords(coord, arr):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    candidates = [add_coords(coord, offset) for offset in offsets]
    neighbors = [c for c in candidates if is_within_bounds(c, arr)]
    return neighbors


def is_low_point(coord, arr):
    neighbor_values = [arr[n] for n in get_neighbor_coords(coord, arr)]
    is_low = arr[coord] < min(neighbor_values)
    return is_low


def get_low_points(arr):
    dim_i, dim_j = arr.shape
    all_coords = product(range(dim_i), range(dim_j))
    lows = [c for c in all_coords if is_low_point(c, arr)]
    return lows


def get_basin(coord, arr):
    unexplored = {coord}
    visited = set()
    basin = set()

    while unexplored:
        coord = unexplored.pop()
        visited.add(coord)
        if arr[coord] != 9:
            basin.add(coord)
            neighbors = get_neighbor_coords(coord, arr)
            for n in neighbors:
                if n not in visited:
                    unexplored.add(n)

    return basin


def solve_2(low_points):
    sizes = [len(get_basin(coord, arr)) for coord in low_points]
    biggest = sorted(sizes)[-3:]
    result = reduce(mul, biggest)
    return result


if __name__ == "__main__":
    arr = get_cleaned_input()
    low_points = get_low_points(arr)

    answer_1 = sum([arr[low] for low in low_points])
    answer_2 = solve_2(low_points)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
