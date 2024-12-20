from itertools import permutations
from utils import read, print_answers


def bfs(floor):
    floor = floor.copy()
    todo = [(0, start)]
    dist = {}
    while todo:
        i, n = todo.pop(0)
        dist[n] = i
        floor -= {n}
        todo += [(i + 1, nn) for d in (1, -1, 1j, -1j) if (nn := n + d) in floor]
    return dist


def l1(a, b):
    return int(abs((a - b).real) + abs((a - b).imag))


def get_dist(w1, w2):
    return D[w1] + l1(w1, w2) + D[end] - D[w2]


def solve(time, thrs):
    warps = [w for w in permutations(floor, 2) if 1 < l1(*w) <= time]
    distances = [d for w in warps if (d := get_dist(*w))]
    return len([d for d in distances if D[end] - d >= thrs])


raw = read(2024, 20).split("\n")

M = {c + 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}
start = next(k for k, v in M.items() if v == "S")
end = next(k for k, v in M.items() if v == "E")
floor = set([k for k, v in M.items() if v != "#"])

D = bfs(floor)

a1 = solve(time=2, thrs=100)
a2 = solve(time=20, thrs=100)

print_answers(a1, a2, day=20)
