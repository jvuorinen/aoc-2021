import re
from collections import defaultdict
from utils import read, print_answers


def splice(cmp):
    return tuple(re.findall(r"[A-Z][a-z]?", cmp))


_d, cmp = read(2015, 19).split("\n\n")
MLC = splice(cmp)

R = defaultdict(list)
for line in _d.split("\n"):
    a, b = line.split(" => ")
    R[a].append(splice(b))

# Part 2 magic numbers
BFS_TODO_SIZE = 100
BUFFER_SIZE = 1


def score(test):
    for i, (a, b) in enumerate(zip(test, MLC)):
        if a != b:
            return i


def get_replacements(mlc, unlimited=False):
    coll = set()

    if unlimited:
        smin, smax = 0, len(mlc)
    else:
        s = score(mlc)
        smin = max(s - BUFFER_SIZE, 0)
        smax = min(s + BUFFER_SIZE, len(mlc))

    for i in range(smin, smax):
        if (m := mlc[i]) in R:
            for r in R.get(m):
                _mlc = mlc[:i] + r + mlc[i + 1 :]
                coll.add(_mlc)
    return coll


def part2():
    todo = [("e",)]
    for i in range(1, 250):
        _todo = set().union(*map(get_replacements, todo))
        if MLC in _todo:
            return i
        _todo = [x for x in _todo if len(x) <= len(MLC)]
        todo = sorted(_todo, key=lambda x: score(x))[-BFS_TODO_SIZE:]


a1 = len(get_replacements(MLC, unlimited=True))
a2 = part2()
print_answers(a1, a2, day=19)
