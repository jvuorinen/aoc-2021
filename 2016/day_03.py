from itertools import chain
from utils import read, print_answers


def is_good(spec):
    a, b, c = sorted(spec)
    return a + b > c


raw = read(2016, 3).split("\n")

original = [[*map(int, line.split())] for line in raw]
flat = [*chain(original)]
flipped = [sorted([flat[i + j] for j in (0, 3, 6)]) for i in range(len(flat)) if i % 9 < 3]

a1 = sum(map(is_good, original))
a2 = sum(map(is_good, flipped))

print_answers(a1, a2, day=3)
