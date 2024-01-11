import re
from dataclasses import dataclass
from utils import print_answers, read

from heapq import heappush, heappop


@dataclass
class Bot:
    loc: tuple[int]
    signal: int


def manhattan(a, b):
    return sum([abs(c1 - c2) for c1, c2 in zip(a, b)])


def in_range(p, bot):
    return manhattan(p, bot.loc) <= bot.signal


def solve_1(bots):
    stronk = max(bots, key=lambda x: x.signal)
    return sum([in_range(b.loc, stronk) for b in bots])


def _octosplit(center, size):
    _size = size / 2
    return [
        ((center[0] + i * _size, center[1] + j * _size, center[2] + k * _size), _size)
        for i in (-1, 1)
        for j in (-1, 1)
        for k in (-1, 1)
    ]


def solve_2(bots):
    center, size = (0, 0, 0), 2**28
    Q = [(1, size, 0, (center, size))]
    best = 0
    while Q:
        maxb, size, _, cube = heappop(Q)
        if size < 1:
            pixel = tuple(map(int, cube[0]))
            n = sum([in_range(pixel, b) for b in bots])
            if n > best:
                best = n
                res = sum(map(abs, pixel))
        elif abs(maxb) >= best:
            for _c, _s in _octosplit(*cube):
                _maxb = sum([manhattan(_c, b.loc) < (_s * 3 + b.signal) for b in bots])
                _d = sum(map(abs, _c))
                heappush(Q, (-_maxb, _s, _d, (_c, _s)))
    return res


bots = []
for line in read("inputs/day_23b.txt").split("\n"):
    a, b = re.findall(r"<(.*)>.* r=(.*)", line)[0]
    bots.append(Bot(tuple(map(int, a.split(","))), int(b)))

a1 = solve_1(bots)
a2 = solve_2(bots)

print_answers(a1, a2, day=23)  # 463 93826293
