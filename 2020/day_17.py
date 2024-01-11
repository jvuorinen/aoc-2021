from itertools import product

from utils import read_input


def parse_coords(raw_in, ndim):
    coords = set()
    for i, l in enumerate(raw_in):
        for j, c in enumerate(l):
            if c == "#":
                coords.add(tuple([i, j] + (ndim - 2) * [0]))
    return coords


def get_neighbors(coord):
    self_included = set(product(*((x - 1, x, x + 1) for x in coord)))
    return self_included - {coord}


def update(coords, ndim):
    new = set()

    for loc in coords:
        n_neighbors = sum((n in coords) for n in get_neighbors(loc))
        if n_neighbors in (2, 3):
            new.add(loc)

    neighboring = set.union(*(get_neighbors(x) for x in coords)) - coords
    for loc in neighboring:
        n_neighbors = sum((n in coords) for n in get_neighbors(loc))
        if n_neighbors == 3:
            new.add(loc)

    return new


def solve(raw_in, ndim, sim_length):
    coords = parse_coords(raw_in, ndim)

    for _ in range(sim_length):
        coords = update(coords, ndim)

    return len(coords)


if __name__ == "__main__":
    raw_in = read_input("inputs/day_17.txt")

    answer_1 = solve(raw_in, ndim=3, sim_length=6)
    answer_2 = solve(raw_in, ndim=4, sim_length=6)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
