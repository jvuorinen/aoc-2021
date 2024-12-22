from utils import read, print_answers

SIZE = 2000
M = 16777216

def step(n):
    n = ((n*64) ^ n ) % M
    n = ((n//32) ^ n ) % M
    return ((n * 2048) ^ n) % M

raw = read(2024, 22).split("\n")

a1 = 0
D = [{} for _ in range(len(raw))]
for i, n in enumerate(map(int, raw)):
    ns = [n] + [(n := step(n)) for _ in range(SIZE)]
    ps = [x % 10 for x in ns]
    ds = [b-a for a, b in zip(ps[:-1], ps[1:])]
    chunks = [tuple(ds[i:i+4]) for i in range(len(ds)-3)]
    a1 += ns[-1]
    for j, c in enumerate(chunks[::-1], 1):
        D[i][c] = ps[-j]

keys = set.union(*[set(d) for d in D])
a2 = max(sum(d.get(k, 0) for d in D) for k in keys)

print_answers(a1, a2, day=22)
# 1931
