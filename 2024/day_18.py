from itertools import product
from utils import read, print_answers

raw = read(2024, 18).split("\n")

drops = []
for line in raw:
    a, b = line.split(",")
    drops.append(int(a) + int(b) * 1j)

W, H = 70, 70
end = (W) + (H) * 1j


def bfs(wait):
    ok = {a + 1j * b for a, b in product(range(W + 1), range(H + 1))}
    ok -= {d for d in drops[: wait + 1]}

    n = 0j
    todo = [(0, 0j)]
    seen = set()
    while todo:
        i, n = todo.pop(0)
        if n == end:
            return i
        for nn in [nn for d in (1, -1, 1j, -1j) if (nn := (n + d)) in ok and nn not in seen]:
            seen.add(nn)
            todo.append((i + 1, nn))


a1 = bfs(1024)

d = drops[next(w for w in range(1, 100000) if bfs(w) is None)]
a2 = f"{int(d.real)},{int(d.imag)}"

print_answers(a1, a2, day=18)
