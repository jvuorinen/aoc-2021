from itertools import product
from utils import read, print_answers


raw = read(2024, 18).split("\n")

drops = [complex(*map(int, x.split(","))) for x in raw]
W, H = 70, 70
end = (W) + (H) * 1j


def bfs(wait):
    ok = {a + 1j * b for a, b in product(range(W + 1), range(H + 1))}
    ok -= {d for d in drops[: wait + 1]}

    todo = [(0, 0j)]
    while todo:
        i, n = todo.pop(0)
        if n == end:
            return i
        for nn in [nn for d in (1, -1, 1j, -1j) if (nn := (n + d)) in ok]:
            ok.remove(nn)
            todo.append((i + 1, nn))


a1 = bfs(1024)

d = drops[next(w for w in range(1, len(drops)) if bfs(w) is None)]
a2 = f"{int(d.real)},{int(d.imag)}"

print_answers(a1, a2, day=18)
