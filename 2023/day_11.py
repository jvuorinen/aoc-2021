from itertools import combinations

import numpy as np
from utils import print_answers, read_file


def get_distance_map(arr, expansion):
    space = arr == "."
    dmap = np.ones_like(arr, dtype=int)
    xs = np.where((space.sum(axis=0) == arr.shape[0]))[0]
    ys = np.where((space.sum(axis=1) == arr.shape[1]))[0]
    dmap[:, xs] = expansion
    dmap[ys, :] = expansion
    return dmap


def get_dist(dmap, a, b):
    y1, y2 = sorted([a[0], b[0]])
    x1, x2 = sorted([a[1], b[1]])
    slice = dmap[y1 : y2 + 1, x1 : x2 + 1]
    path = list(slice[0, :]) + list(slice[:, -1][1:])
    return sum(map(int, path[1:]))


def sum_shortest_paths(gals, dmap):
    return sum([get_dist(dmap, a, b) for a, b in combinations(gals, 2)])


raw_in = read_file("inputs/day_11b.txt").split("\n")
arr = np.array([list(x) for x in raw_in])
gals = [(a, b) for a, b in zip(*np.where(arr == "#"))]

a1 = sum_shortest_paths(gals, get_distance_map(arr, 2))
a2 = sum_shortest_paths(gals, get_distance_map(arr, 1000000))

print_answers(a1, a2, day=11)  # Correct: 9974721, 702770569197
