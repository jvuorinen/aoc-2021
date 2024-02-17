from hashlib import md5
from utils import read, print_answers

DIRS = {"U": -1j, "D": 1j, "L": -1, "R": 1}
CODE = read(2016, 17)


def is_legit(loc):
    return all(0 <= x <= 3 for x in (loc.real, loc.imag))


def get_dirs(loc, path):
    hsh = md5((CODE + path).encode()).hexdigest()[:4]
    return [d for d, h in zip(DIRS.keys(), hsh) if h in "bcdef" and is_legit(loc + DIRS[d])]


solutions = set()
seen = set()
Q = [(0j, "")]
while Q:
    loc, path = Q.pop(0)
    seen.add((loc, path))
    if loc == 3 + 3j:
        solutions.add(path)
    else:
        for d in get_dirs(loc, path):
            _loc = loc + DIRS[d]
            _path = path + d
            if (_loc, _path) not in seen:
                Q.append((_loc, _path))

a1 = min(solutions, key=len)
a2 = max(map(len, solutions))

print_answers(a1, a2, day=17)
