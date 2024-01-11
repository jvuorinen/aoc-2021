from utils import read_file, print_answers
import json
from itertools import chain
from functools import cmp_to_key
from math import prod


def compare(pair):
    match pair:
        case int(a), int(b):
            if a < b:
                return True
            if a > b:
                return False
        case int(a), list(b):
            return compare([[a], b])
        case list(a), int(b):
            return compare([a, [b]])
        case list(a), list(b):
            for aa, bb in zip(a, b):
                check = compare([aa, bb])
                if check is not None:
                    return check
            if len(a) < len(b):
                return True
            if len(a) > len(b):
                return False


if __name__ == "__main__":
    raw_in = read_file("inputs/day_13b.txt")
    pairs = [list(map(json.loads, r.split())) for r in raw_in.split("\n\n")]

    # Part 1
    checks = [compare(p) for p in pairs]
    a1 = sum([i for i, ok in enumerate(checks, 1) if ok])

    # Part 2
    dividers = [[[2]], [[6]]]
    full = list(chain(*pairs)) + dividers
    ordered = sorted(full, key=cmp_to_key(lambda a, b: -1 if compare([a, b]) else 1))
    a2 = prod([1 + ordered.index(d) for d in dividers])

    print_answers(a1, a2, day=13)
