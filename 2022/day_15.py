from utils import read_file, print_answers
from itertools import combinations
import re


def parse(raw_in):
    get_nums = lambda r: [int(x) for x in re.findall("=(.{0,1}\d+)", r)]
    nums = [get_nums(r) for r in raw_in]
    closest = [((a, b), (c, d)) for a, b, c, d in nums]
    return closest


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _get_scanner_impossibles_x(b, c, y):
    total = dist(b, c)
    rlen = total - abs(b[1] - y)
    res = (b[0] - rlen, b[0] + rlen) if (rlen > 0) else ()
    return res


def _combine_ranges(r1, r2):
    (a0, a1), (b0, b1) = r1, r2

    if (a0 - b1 > 1) or (b0 - a1 > 1):
        return [r1, r2], False
    else:
        each = list(r1) + list(r2)
        return [(min(each), max(each))], True


def fuse(ranges):
    for p in combinations(ranges, 2):
        c, merged = _combine_ranges(*p)
        if merged:
            new = c + [x for x in ranges if x not in p]
            return fuse(new)
    return ranges


def get_impossibles_y(closest, y):
    ranges = [_get_scanner_impossibles_x(b, c, y) for b, c in closest]
    ranges = [x for x in ranges if len(x) > 0]
    fused = fuse(ranges)
    return fused


def solve_1(closest, threshold):
    impossibles = get_impossibles_y(closest, threshold // 2)
    return sum([r[1] - r[0] for r in impossibles])


def _get_lines(s, b):
    x, y = s
    d = dist(s, b) + 1
    return [
        (y - x - d, 1),
        (y - x + d, 1),
        (y + x - d, -1),
        (y + x + d, -1),
    ]


def solve_2(closest):
    # Find the 2 pairs of scanners leaving a width-1 line between them
    check = lambda a, b: dist(a[0], b[0]) - dist(*a) - dist(*b) == 2
    pairs = [p for p in combinations(closest, 2) if check(*p)]

    # Find the in-between line for both pairs
    find_common = lambda a, b: set(_get_lines(*a)) & set(_get_lines(*b))
    lines = [find_common(*p).pop() for p in pairs]

    # Find the intersection of the two lines
    (a1, b1), (a2, b2) = lines
    x = (a2 - a1) // (b1 - b2)
    y = a1 + b1 * x
    return x * 4_000_000 + y


if __name__ == "__main__":
    THRS = 4_000_000

    raw_in = read_file("inputs/day_15b.txt").split("\n")
    closest = parse(raw_in)

    a1 = solve_1(closest, THRS)
    a2 = solve_2(closest)

    print_answers(a1, a2, day=15)
