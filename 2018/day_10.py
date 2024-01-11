import re
import numpy as np
from utils import read, print_answers


def parse():
    pos, vel = [], []
    for line in read("inputs/day_10b.txt").split("\n"):
        a, b, c, d = map(int, re.findall(r"(-?\d+)", line))
        pos.append(complex(a, b))
        vel.append(complex(c, d))
    return np.array(pos), np.array(vel)


def draw(pos):
    shape_y = int(max(pos.imag) - min(pos.imag)) + 1
    shape_x = int(max(pos.real) - min(pos.real)) + 1

    arr = [[" "] * shape_x for _ in range(shape_y)]
    for c in pos - complex(min(pos.real), min(pos.imag)):
        arr[int(c.imag)][int(c.real)] = "#"
    return "\n".join(map("".join, arr))


pos, vel = parse()

i = 0
while max(pos.imag) - min(pos.imag) > 10:
    pos += vel
    i += 1

a1 = i
a2 = draw(pos)
print_answers(a1, a2, day=10)
