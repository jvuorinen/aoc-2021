from math import prod
from utils import read, print_answers


PRESENTS = tuple(map(int, read(2015, 24).split("\n")))[::-1]


def knapsack(presents, target, maxlen=1e12, chosen=None):
    chosen = chosen or tuple()
    if (s := sum(chosen)) == target:
        yield tuple(chosen)
    if presents and (s < target) and len(chosen) < maxlen:
        first, rest = presents[0], presents[1:]
        yield from knapsack(rest, target, maxlen, chosen + (first,))
        yield from knapsack(rest, target, maxlen, chosen)


def evaluate(g, size, ps=None):
    ps = ps if ps is not None else set(PRESENTS) - set(g)
    if not ps:
        return True
    for _g in knapsack(sorted(ps)[::-1], size):
        if evaluate(_g, size, ps - set(_g)):
            return prod(g)


def solve(n_groups):
    size = sum(PRESENTS) // n_groups
    for i in range(100):
        if candidates := [*knapsack(PRESENTS, size, maxlen=i)]:
            return min([evaluate(c, size) for c in candidates])


print_answers(solve(3), solve(4), day=24)
