import numpy as np
from utils import read, print_answers

# raw = read().split("\n")
raw = read(2024, 4).split("\n")

arr = np.array([list(x) for x in raw])

a1  = 0
for _ in range(4):
    for line in arr:
        txt = "".join(line)
        a1 += txt.count("XMAS")
    for i in range(0-len(arr), len(arr)):
        txt = "".join(np.diag(arr, i))
        a1 += txt.count("XMAS")
    arr = np.rot90(arr)

a2 = 0
for i in range(len(arr) - 2):
    for j in range(len(arr)-2):
        slice = arr[i:i+3, j:j+3]
        d1 = "".join(np.diag(slice))
        d2 = "".join(np.diag(np.rot90(slice)))
        if d1 in ("SAM", "MAS") and d2 in ("SAM", "MAS"):
            a2 += 1


print_answers(a1, a2, day=4)
