from collections import Counter
from utils import read, print_answers


def step(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    return ((n * 2048) ^ n) % 16777216


raw = read(2024, 22).split("\n")

a1 = 0
D = [{} for _ in range(len(raw))]
for i, n in enumerate(map(int, raw)):
    ns = [n] + [(n := step(n)) for _ in range(2000)]
    a1 += ns[-1]
    ps = [x % 10 for x in ns]
    ds = [b - a for a, b in zip(ps[:-1], ps[1:])]
    chunks = [tuple(ds[i : i + 4]) for i in range(len(ds) - 3)]
    for j, c in enumerate(chunks[::-1], 1):
        D[i][c] = ps[-j]

cnt = Counter(tuple(x) for d in D for x in d)
best = sorted(cnt, key=cnt.get)[-100:]
a2 = max(sum(d.get(k, 0) for d in D) for k in best)

print_answers(a1, a2, day=22)
