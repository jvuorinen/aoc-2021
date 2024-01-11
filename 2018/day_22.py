from functools import cache
from heapq import heappush, heappop
from itertools import count
from utils import print_answers

DPT = 8787
T = 10 + 725j


@cache
def erosion(loc):
    if loc.real == 0:
        return int(48271 * loc.imag + DPT) % 20183
    if loc.imag == 0:
        return int(16807 * loc.real + DPT) % 20183
    return (erosion(loc - 1) * erosion(loc - 1j) + DPT) % 20183


risk = {
    (loc := x + y * 1j): erosion(loc) % 3
    for x in range(int(T.real) + 50)
    for y in range(int(T.imag) + 50)
}
risk[T] = 0

VALID = {0: {"T", "G"}, 1: {"G", "N"}, 2: {"T", "N"}}


def get_actions(loc, eq):
    moves = [
        (1, (nxt, eq))
        for d in [1, -1, 1j, -1j]
        if (nxt := loc + d) in risk and (eq in VALID[risk[nxt]])
    ]
    swap = [(7, (loc, list(VALID[risk[loc]] - {eq})[0]))]
    return moves + swap


def crawl():
    start = (0j, "T")
    goal = (T, "T")
    n = count()
    Q = [(0, next(n), start)]
    seen = {}

    while Q:
        t, _, state = heappop(Q)
        if state == goal:
            return t
        if state not in seen:
            seen[state] = t
            for td, _st in get_actions(*state):
                heappush(Q, (t + td, next(n), _st))


a1 = sum([v for x, v in risk.items() if (x.real <= T.real) and (x.imag <= T.imag)])
a2 = crawl()
print_answers(a1, a2, day=22)  # 8090 992
