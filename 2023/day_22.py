from functools import cache
from utils import read_file, print_answers, add_coords


@cache
def get_range(c1, c2):
    if c1 == c2:
        return [c1]
    ax, r = [(i, abs(a - b)) for i, (a, b) in enumerate(zip(c1, c2)) if a != b][0]
    c = min(c1, c2)
    to_add = tuple(1 if i == ax else 0 for i in range(3))
    return [c] + [c := add_coords(c, to_add) for _ in range(r)]


def get_moving(bricks):
    occupied = {}
    for i, (a, b) in enumerate(bricks):
        for loc in get_range(a, b):
            occupied[loc] = i
    moving = []
    for i, (a, b) in enumerate(bricks):
        for loc in get_range(a, b):
            under = occupied.get(add_coords(loc, (0, 0, -1)))
            if (loc[2] == 1) or (under not in (None, i)):
                break
        else:
            moving.append(i)
    return moving


def make_fall(bricks):
    has_moved = set()
    while moving := get_moving(bricks):
        for i in moving:
            has_moved.add(i)
            bricks[i] = [add_coords(bricks[i][x], (0, 0, -1)) for x in (0, 1)]
    return len(has_moved)


def get_counts(bricks):
    nfall = {}
    for i, _ in enumerate(bricks):
        _bricks = bricks.copy()
        _bricks.pop(i)
        nfall[i] = make_fall(_bricks)
    return nfall


if __name__ == "__main__":
    raw_in = read_file("inputs/day_22b.txt").split("\n")
    bricks = [tuple([tuple([*map(int, x.split(","))]) for x in r.split("~")]) for r in raw_in]

    make_fall(bricks)
    nfall = get_counts(bricks)

    a1 = sum([v == 0 for v in nfall.values()])
    a2 = sum(nfall.values())

    print_answers(a1, a2, day=22)  # Correct: 495, 76158
