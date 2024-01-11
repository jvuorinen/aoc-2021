from utils import read_file, print_answers

P1 = {
    "A": "R",
    "B": "P",
    "C": "S",
}

SCORE_SHAPE = {
    "R": 1,
    "P": 2,
    "S": 3,
}

OUTCOME = {
    ("R", "R"): 0,
    ("R", "P"): 1,
    ("R", "S"): -1,
    ("P", "R"): -1,
    ("P", "P"): 0,
    ("P", "S"): 1,
    ("S", "R"): 1,
    ("S", "P"): -1,
    ("S", "S"): 0,
}


def get_shapes_1(r):
    a, b = r.split(" ")

    p1 = P1[a]
    p2 = {"X": "R", "Y": "P", "Z": "S"}[b]
    return p1, p2


def get_shapes_2(r):
    a, b = r.split(" ")

    p1 = P1[a]
    desired = {"X": -1, "Y": 0, "Z": 1}[b]
    inverted = {(p1, o): p2 for (p1, p2), o in OUTCOME.items()}
    p2 = inverted[(p1, desired)]
    return p1, p2


def score_game(p1, p2):
    return 3 * OUTCOME[(p1, p2)] + 3


def score(r, get_shapes_func):
    p1, p2 = get_shapes_func(r)
    return SCORE_SHAPE[p2] + score_game(p1, p2)


if __name__ == "__main__":
    raw_in = read_file("inputs/day_02.txt").split("\n")

    a1 = sum([score(r, get_shapes_1) for r in raw_in])
    a2 = sum([score(r, get_shapes_2) for r in raw_in])

    print_answers(a1, a2, day=2)
