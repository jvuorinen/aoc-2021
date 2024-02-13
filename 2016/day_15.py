import re
from utils import read, print_answers


def naive_crt(remainders, mods):
    x, s = 0, 1
    for r, m in zip(remainders, mods):
        while x % m != r:
            x += s
        s *= m
    return x


def solve(mods, pos):
    remainders = [(-p - i) % m for i, (p, m) in enumerate(zip(pos, mods), 1)]
    return naive_crt(remainders, mods)


raw = read(2016, 15).split("\n")

pat = r"has (\d+) positions; at time=0, it is at position (\d+)"
mods, pos = map(list, zip(*[map(int, re.findall(pat, line)[0]) for line in raw]))

a1 = solve(mods, pos)
a2 = solve(mods + [11], pos + [0])

print_answers(a1, a2, day=15)  # 121834 3208099
