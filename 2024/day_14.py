from math import prod
from itertools import product
from re import findall
from utils import read, print_answers


W, H = 101, 103
Q = [*product(*[[(0, d // 2 - 1), (d // 2 + 1, d)] for d in (W, H)])]

raw = read(2024, 14)
ints = [map(int, findall(r"\-?\d+", line)) for line in raw.split("\n")]
ps, vs = zip(*[(x + 1j * y, vx + 1j * vy) for x, y, vx, vy in ints])


def simulate(ps, vs, n):
    noclip = [p + n * v for p, v in zip(ps, vs)]
    return [complex(z.real % W, z.imag % H) for z in noclip]


def in_bounds(z, br1, br2, bi1, bi2):
    return (br1 <= z.real <= br2) and (bi1 <= z.imag <= bi2)


def get_quadrants_counts(ps):
    return [sum(in_bounds(z, a, b, c, d) for z in ps) for (a, b), (c, d) in Q]


def draw(ps):
    area = [["#" if (x + y * 1j in ps) else "." for x in range(W)] for y in range(H)]
    print("\n".join(map("".join, area)))


a1 = prod(get_quadrants_counts(simulate(ps, vs, 100)))

tests = [get_quadrants_counts(simulate(ps, vs, i)) for i in range(10_000)]
a2, _ = max(enumerate(tests), key=lambda x: max(x[1]))

# draw(simulate(ps, vs, a2))
print_answers(a1, a2, day=14)
