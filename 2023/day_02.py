import re
from math import prod
from utils import read_file, print_answers


def parse_game(row):
    counts = [re.findall(r"(\d*) (red|green|blue)", x) for x in row.split(";")]
    return [dict([(x[1], int(x[0])) for x in row]) for row in counts]


def is_possible(game, bag):
    return all([all([x.get(c, 0) <= bag[c] for c in bag.keys()]) for x in game])


def get_mins(game):
    return {c: max([x.get(c, 0) for x in game]) for c in ("red", "green", "blue")}


if __name__ == "__main__":
    raw_in = read_file("inputs/day_02.txt").split("\n")
    games = [parse_game(row) for row in raw_in]

    bag = {"red": 12, "green": 13, "blue": 14}

    a1 = sum([i for i, g in enumerate(games, 1) if is_possible(g, bag)])
    a2 = sum([prod(get_mins(g).values()) for g in games])

    print_answers(a1, a2, day=2)  # Correct: 2278, 67953
