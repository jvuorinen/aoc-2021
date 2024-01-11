from math import prod
from utils import read_file, print_answers


def _get_dist(t, w):
    return (t - w) * w


def solve(t, d):
    a, b = 0, t  # a, b are binary search bounds
    while b - a > 1:
        w = (a + b) // 2
        a, b = (a, w) if _get_dist(t, w) > d else (w, b)
    correction = -1 if (t % 2 == 0) else 0
    return (t // 2 - a) * 2 + correction


a, b = read_file("inputs/day_06b.txt").split("\n")
ts = [int(x) for x in a.split(": ")[1].split()]
ds = [int(x) for x in b.split(": ")[1].split()]

# Part 1
a1 = prod([solve(t, d) for t, d in zip(ts, ds)])

# Part 2
t = int("".join(map(str, ts)))
d = int("".join(map(str, ds)))
a2 = solve(t, d)

print_answers(a1, a2, day=6)  # Correct: 227850, 42948149
