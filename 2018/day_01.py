from utils import read, print_answers
from itertools import accumulate, cycle


def p2(ds):
    seen = set([])
    for f in accumulate(cycle(ds)):
        if f in seen:
            return f
        else:
            seen.add(f)


ds = [int(x) for x in read("inputs/day_01.txt").split()]

a1 = sum(ds)
a2 = p2(ds)
print_answers(a1, a2, day=1)
