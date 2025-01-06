from itertools import groupby
from utils import read, print_answers
from string import ascii_lowercase as ABC

BASE = len(ABC)


def n_to_baserep(n, base):
    while n:
        n, m = divmod(n, base)
        yield m


def baserep_to_n(br, base):
    return sum(x * base**i for i, x in enumerate(br))


def check(n):
    br = list(n_to_baserep(n, BASE))
    if (1, 2) not in ((a - b, a - c) for a, b, c in zip(br[:-2], br[1:-1], br[2:])):
        return False
    if len({n for n, g in groupby(br) if len(list(g)) >= 2}) <= 1:
        return False
    return not set(br) & set(map(ABC.index, "iol"))


def rotator(pw):
    br = [ord(x) - ord("a") for x in pw[::-1]]
    n = baserep_to_n(br, BASE)
    for i in range(1, int(1e12)):
        if check(n + i):
            yield "".join(ABC[x] for x in n_to_baserep(n + i, BASE))[::-1]


pw = read(2015, 11)
gen = rotator(pw)

print_answers(next(gen), next(gen), day=11)
