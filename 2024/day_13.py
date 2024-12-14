from re import findall
import numpy as np
from utils import read, print_answers

raw = read(2024, 13).split("\n\n")

ans = [0, 0]
for line in raw:
    nums = [*map(int, findall(r"\d+", line))]

    X = np.array([nums[0:2], nums[2:4]]).T
    y = np.array([nums[4:]]).T

    for i, y in enumerate([y, y + 10000000000000]):
        res = np.linalg.solve(X, y).round().astype(int)
        if all(X @ res == y):
            ans[i] += np.dot(res.T, [3, 1])[0]


print_answers(ans[0], ans[1], day=13)
