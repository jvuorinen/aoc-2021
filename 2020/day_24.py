import re

from utils import read_input

COORDS = {
    "e": (0, 2),
    "se": (-2, 1),
    "sw": (-2, -1),
    "w": (0, -2),
    "nw": (2, -1),
    "ne": (2, 1),
}


def parse_instructions(raw_in):
    parse_line = lambda line: [x for x in re.findall(r"(e|se|sw|w|nw|ne)", line)]
    return [parse_line(line) for line in raw_in]


def create_floor(instructions):
    floor = set()
    for path in instructions:
        x, y = (0, 0)
        for c in path:
            dx, dy = COORDS[c]
            x += dx
            y += dy
        if (x, y) in floor:
            floor.remove((x, y))
        else:
            floor.add((x, y))
    return floor


def _get_neighbors(loc):
    x, y = loc
    return set((x + dx, y + dy) for dx, dy in COORDS.values())


def _update(floor):
    new = set()

    for loc in floor:
        n_neighbors = sum((n in floor) for n in _get_neighbors(loc))
        if n_neighbors in (1, 2):
            new.add(loc)

    neighboring = set.union(*(_get_neighbors(x) for x in floor)) - floor
    for loc in neighboring:
        n_neighbors = sum((n in floor) for n in _get_neighbors(loc))
        if n_neighbors == 2:
            new.add(loc)

    return new


def solve_2(floor):
    for _ in range(100):
        floor = _update(floor)
    return len(floor)


if __name__ == "__main__":
    raw_in = read_input("inputs/day_24.txt")
    instructions = parse_instructions(raw_in)

    floor = create_floor(instructions)

    answer_1 = len(floor)
    answer_2 = solve_2(floor)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
