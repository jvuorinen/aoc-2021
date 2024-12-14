from math import prod
from itertools import product
from re import findall
from utils import read, print_answers


W, H = 101, 103
Q = [*product([(0, W // 2), (W // 2 + 2, W)], [(0, H // 2), (H // 2 + 2, H)])]


raw = read(2024, 14).split("\n")
ps, vs = [], []
for line in raw:
    x, y, vx, vy = map(int, findall(r"\-?\d+", line))
    ps.append(x + 1j * y)
    vs.append(vx + 1j * vy)


def simulate(ps, vs, n):
    noclip = [p + n * v for p, v in zip(ps, vs)]
    return [complex(z.real % W, z.imag % H) for z in noclip]


def in_bounds(z, br1, br2, bi1, bi2):
    return (br1 <= z.real <= br2) and (bi1 <= z.imag <= bi2)


def get_quadrants_counts(robots):
    return [sum(in_bounds(r, a, b, c, d) for r in robots) for (a, b), (c, d) in Q]


def draw(ps):
    area = [["#" if (x + y*1j in ps) else "." for x in range(W)] for y in range(H)]
    print("\n".join(map("".join, area)))


a1 = prod(get_quadrants_counts(simulate(ps, vs, 100)))

# tests = [get_quadrants_counts(simulate(ps, vs, i)) for i in range(10_000)]
# a2, _ = max(enumerate(tests), key=lambda x: max(x[1]))
a2 = None

# draw(simulate(ps, vs, a2))
print_answers(a1, a2, day=14)
