import numpy as np
from re import findall
from utils import read, print_answers

# raw = read().split("\n\n")
raw = read(2024, 13).split("\n\n")

xs, ys = [], []
for line in raw:
    nums = [*map(int, findall(r'\d+', line))]
    xs.append(np.array([nums[0:2], nums[2:4]]).T)
    ys.append(np.array([nums[4:]]).T)

funny, results = list(), list()

a1 = 0
for x, y in zip(xs, ys):
    y += 10000000000000
    res = np.linalg.solve(x, y)
    a = res[0][0]
    b = res[1][0]

    # tst =  x[1] / x[0]
    # if tst[0] == tst[1] :
    #     print(x)
    # print()
    # print(x, y, res)

    tst = x @ res.round()
    if all(tst == y):
        a1 += round(3*a) + round(b)
        results.append(res)
    else:
        funny.append(res)
        # print(res)
    # np.linalg.solve()


a2 = None

print_answers(a1, a2, day=13)
# 32026