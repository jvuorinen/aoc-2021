from itertools import permutations
from re import findall
from utils import read, print_answers


lines = read(2016, 22).split("\n")

nodes = []
for line in lines[2:]:
    name, rest = line.split(' ', 1)
    coords = complex(*map(int, findall(r"\d+", name)))
    _, used, av, _ = map(int, findall(r"\d+", rest))
    nodes += [(coords, int(used), int(av))]

a1 = sum([1 for a, b in permutations(nodes, 2) if a[1] and a[1] <= b[2]])


free = next(n[0] for n in nodes if n[1] == 0)
tgt = max(z[0].real for z in nodes) + 0j
movable = [n[0] for n in nodes if n[1] < 100]


a2 = None
print_answers(a1, a2, day=22)
