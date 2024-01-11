import re
from dataclasses import dataclass
from functools import reduce
from operator import mul

from tqdm import tqdm

from utils import read_input


@dataclass
class HyperCube:
    dims: list[tuple[int, int]]
    state: str


def get_copy(c: HyperCube):
    return HyperCube(c.dims[:], c.state)


def get_volume(c: HyperCube):
    res = reduce(mul, [(d2 - d1 + 1) for d1, d2 in c.dims])
    return res


def lines_overlapping(a1, a2, b1, b2):
    not_overlapping = (a2 <= b1) or (b2 <= a1)
    res = not not_overlapping
    return res


def cubes_overlapping(c1, c2):
    dim_overlaps = [
        lines_overlapping(d1[0], d1[1], d2[0], d2[1]) for d1, d2 in zip(c1.dims, c2.dims)
    ]
    res = all(dim_overlaps)
    return res


def _split(cube, dim, split_point):
    low, high = cube.dims[dim]
    assert low < split_point <= high

    h1 = get_copy(cube)
    h2 = get_copy(cube)

    h1.dims[dim] = (low, split_point - 1)
    h2.dims[dim] = (split_point, high)
    return h1, h2


def _shatter_by_dim(cube_1, cube_2, dim):
    """Returns only pieces of cube_1 (not cube_2)"""
    pieces = []

    first, last = cube_1.dims[dim]
    split_candidates = (cube_2.dims[dim][0], cube_2.dims[dim][1] + 1)
    split_points = [x for x in split_candidates if (first < x <= last)][::-1]
    rest = get_copy(cube_1)
    while split_points:
        sp = split_points.pop()
        p, rest = _split(rest, dim, sp)
        pieces.append(p)
    pieces.append(rest)

    return pieces


def flatten(_list):
    return sum(_list, [])


def shatter(cube_1, cube_2):
    """Returns only pieces of v1 (not v2)"""
    pieces = [cube_1]

    for dim in range(len(cube_1.dims)):
        pieces_of_pieces = [_shatter_by_dim(p, cube_2, dim) for p in pieces]
        pieces = flatten(pieces_of_pieces)

    return pieces


def get_initial_hypercube(seq):
    xd = flatten([list(v.dims[0]) for v in seq])
    yd = flatten([list(v.dims[1]) for v in seq])
    zd = flatten([list(v.dims[2]) for v in seq])

    dims = [(min(xd), max(xd)), (min(yd), max(yd)), (min(zd), max(zd))]
    v = HyperCube(dims, "off")
    return v


def filter_overlapping(cubes, new):
    overlapping = []
    non_overlapping = []
    for c in cubes:
        if cubes_overlapping(c, new):
            overlapping.append(c)
        else:
            non_overlapping.append(c)
    return overlapping, non_overlapping


def solve(seq):
    cubes = [get_initial_hypercube(seq)]

    for new in tqdm(seq, ascii=True, ncols=80):
        overlapping, cubes = filter_overlapping(cubes, new)
        cubes.append(new)

        for old in overlapping:
            pieces_old = shatter(old, new)
            non_overlapping_old = [p for p in pieces_old if not cubes_overlapping(p, new)]
            cubes.extend(non_overlapping_old)

    res = sum(get_volume(c) for c in cubes if (c.state == "on"))
    return res


def parse_line(line):
    a, b = line.split()
    x1, x2, y1, y2, z1, z2 = map(int, re.findall(r"-?\d+", b))
    t = HyperCube(dims=[(x1, x2), (y1, y2), (z1, z2)], state=a)
    return t


def get_cleaned_input():
    raw_in = read_input("inputs/day_22.txt")
    seq = [parse_line(line) for line in raw_in]
    return seq


if __name__ == "__main__":
    seq = get_cleaned_input()

    init_area = HyperCube([(-50, 50), (-50, 50), (-50, 50)], "off")
    init_seq = [v for v in seq if cubes_overlapping(v, init_area)]

    answer_1 = solve(init_seq)
    answer_2 = solve(seq)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
