from collections import Counter

import numpy as np
from utils import _add_coords, print_answers, read_file

DIRS = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

_add_dir = lambda a, b: _add_coords(DIRS[a], DIRS[b])
_combo = lambda a, b, c: [DIRS[a], _add_dir(a, b), _add_dir(a, c)]
NBS = {
    "N": _combo("N", "E", "W"),
    "S": _combo("S", "E", "W"),
    "E": _combo("E", "N", "S"),
    "W": _combo("W", "N", "S"),
}
ALL_NBS = set.union(*[set(x) for x in NBS.values()])


def get_nbs(c, dir=None):
    if dir is None:
        return [_add_coords(c, x) for x in ALL_NBS]
    else:
        return [_add_coords(c, x) for x in NBS[dir]]


def get_proposition(e, occupied, order):
    for d in order:
        if all((n not in occupied) for n in get_nbs(e, d)):
            return _add_coords(e, DIRS[d])


def get_valid_propositions(proposed):
    counts = Counter(proposed.values())
    return set([a for a, b in counts.items() if b == 1])


def step(elves, order):
    elves = elves.copy()

    occupied = set(elves)
    proposed = {}
    for i, e in enumerate(elves):
        if any(n in occupied for n in get_nbs(e)):
            p = get_proposition(e, occupied, order)
            if p is not None:
                proposed[i] = p

    valid_propositions = get_valid_propositions(proposed)
    for i, p in proposed.items():
        if p in valid_propositions:
            elves[i] = p

    order = order[1:] + order[:1]

    finished = len(valid_propositions) == 0
    return elves, order, finished


def parse(raw_in):
    arr = np.array([list(x) for x in raw_in.split("\n")])
    return list(zip(*np.where(arr == "#")))


def get_range(elves):
    ys, xs = zip(*elves)
    yr = max(ys) - min(ys) + 1
    xr = max(xs) - min(xs) + 1
    return yr, xr


def draw(elves):
    ys, xs = zip(*elves)
    yr, xr = get_range(elves)
    arr = np.zeros((yr, xr), dtype=str)
    arr[:] = "."
    for y, x in elves:
        arr[y - min(ys), x - min(xs)] = "#"
    print("\n".join(map("".join, arr)))


def calculate_area(elves):
    yr, xr = get_range(elves)
    return yr * xr - len(elves)


def simulate(elves, checkpoint):
    order = "NSWE"
    failsafe = 5_000

    for i in range(failsafe):
        if i == checkpoint:
            a1 = calculate_area(elves)
        elves, order, finished = step(elves, order)
        if finished:
            return a1, i + 1


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_23b.txt")
    elves = parse(raw_in)
    # draw(elves)

    a1, a2 = simulate(elves, checkpoint=10)
    print_answers(a1, a2, day=None)
