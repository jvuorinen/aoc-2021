import numpy as np


def read_file(fp):
    with open(fp) as fh:
        result = fh.read()
    return result


def print_answers(a1, a2, day):
    print(f"== Day {day} ==")
    print(a1)
    print(a2)
    print()


# Coordinate utils

Coordinate = tuple[int, ...]
Bounds = list[tuple[int, int]]


def _add_coords(c1: Coordinate, c2: Coordinate) -> Coordinate:
    return tuple([sum(dim) for dim in zip(c1, c2)])


def _is_within_bounds(c: Coordinate, bounds: Bounds) -> bool:
    return all([(bounds[d][0] <= c[d] <= bounds[d][1]) for d in range(len(c))])


def get_neighbors(c: Coordinate, bounds: Bounds = None) -> list[Coordinate]:
    dims = len(c)
    offsets = [tuple([0] * d + [x] + [0] * (dims - d - 1)) for x in (-1, 1) for d in range(dims)]
    ns = [_add_coords(c, o) for o in offsets]
    if bounds:
        ns = [n for n in ns if _is_within_bounds(n, bounds)]
    return ns


def get_bounds(
    arr: np.array,
) -> Bounds:
    return [(0, x - 1) for x in arr.shape]


# Other things


def memoize(func):
    mem = {}

    def inner(*args):
        mem_key = tuple(args)
        if mem_key not in mem:
            mem[mem_key] = func(*args)
        return mem[mem_key]

    return inner
