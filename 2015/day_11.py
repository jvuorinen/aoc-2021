from itertools import groupby
from utils import read, print_answers
from string import ascii_lowercase as ABC

BASE = len(ABC)

def baserep(n, base):
    while n:
        n, m = divmod(n, base)
        yield m

def to_int(br, base):
    return sum(x * base**i for i, x in enumerate(br))

def check(n):
    br = list(baserep(n, BASE))
    if set(br) & set(map(ABC.index, "iol")):
        return False
    if (1, 2) not in [(a-b, a-c) for a, b, c in zip(br[:-2], br[1:-1], br[2:])]:
        return False
    return len({n for n, g in groupby(br) if len(list(g)) >= 2}) > 1


def rotate(pw):
    br = [ord(x) - ord("a") for x in pw[::-1]]
    n = to_int(br, BASE)

    for i in range(1, int(1E12)):
        if check(n+i):
            yield "".join(ABC[x] for x in baserep(n+i, BASE))[::-1]


pw = read(2015, 11)
gen = rotate(pw)

print_answers(next(gen), next(gen), day=11)
