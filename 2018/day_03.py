import numpy as np
import re
from utils import read, print_answers


def load():
    claims = [
        tuple(map(int, re.findall(r"\d+", line))) for line in read("inputs/day_03.txt").split("\n")
    ]

    arr = np.zeros((1000, 1000), int)
    for _, x, y, dx, dy in claims:
        arr[y : y + dy, x : x + dx] += 1
    return claims, arr


def p2(claims, arr):
    for i, x, y, dx, dy in claims:
        if np.all(arr[y : y + dy, x : x + dx] == 1):
            return i


claims, arr = load()

a1 = (arr >= 2).sum()
a2 = p2(claims, arr)
print_answers(a1, a2, day=3)
