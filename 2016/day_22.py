from itertools import permutations
from re import findall
from utils import read, print_answers


lines = read(2016, 22).split("\n")

nodes = []
for line in lines[2:]:
    name, rest = line.split(" ", 1)
    coords = complex(*map(int, findall(r"\d+", name)))
    _, used, av, _ = map(int, findall(r"\d+", rest))
    nodes += [(coords, int(used), int(av))]


def solve(nodes):
    free = next(n[0] for n in nodes if n[1] == 0)
    tgt = max(z[0].real for z in nodes) + 0j
    movable = [n[0] for n in nodes if n[1] < 100]

    todo = [(free, tgt)]
    seen = set()
    for i in range(1000):
        _todo = set()
        for f, t in todo:
            if t == 0:
                return i
            seen.add((f, t))
            for _f in [_f for d in [1, -1, 1j, -1j] if (_f := f + d) in movable]:
                _st = (_f, f if _f == t else t)
                if _st not in seen:
                    _todo.add(_st)
        todo = sorted(list(_todo), key=lambda x: abs(x[1]) + abs(x[1] - x[0]))[:20]


a1 = sum([1 for a, b in permutations(nodes, 2) if a[1] and a[1] <= b[2]])
a2 = solve(nodes)
print_answers(a1, a2, day=22)
