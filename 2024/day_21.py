from itertools import permutations
from functools import cache
from re import findall
from utils import read, print_answers


NUM = {x: c - 1j * r for r, line in enumerate(["789","456", "123", "x0A"]) for c, x in enumerate(line) if x != "x"}
DIR = {x: c - 1j * r for r, line in enumerate(["x^A", "<v>"]) for c, x in enumerate(line) if x != "x"}
D = {-1: "<", 1: ">", 1j: "^", -1j: "v"}


def get_paths(pad, fr, to, paths = None):
    paths = paths or set()
    d = pad[to] - pad[fr]
    rev = {v:k for k, v in pad.items()}
    
    mr = int(abs(d.real))
    dr = int(d.real / mr) if mr else 0
    mi = int(abs(d.imag))
    di = int(d.imag / mi) if mi else 0
    
    for prm in permutations([dr] * mr + [1j*di] * mi):
        tst = pad[fr]
        path = []
        for dd in prm:
            tst += dd
            if tst not in rev:
                break
            path += D[dd]
        else:
            paths.add("".join(path) + "A")
    return paths


@cache
def shortest(seq, depth):
    pad = DIR if any([ch in seq for ch in "<>^v"]) else NUM
    possible = [get_paths(pad, fr, to) for fr, to in zip(seq[:-1], seq[1:])]
    if depth == 0:
        return sum([min(map(len, s)) for s in possible])
    return sum(min([shortest("A" + x, depth-1) for x in s]) for s in possible)


def get_complexity(code, depth):
    return int(findall(r"\d+", code)[0]) * shortest("A" + code, depth)


codes = read(2024, 21).split("\n")

a1 = sum(get_complexity(c, 2) for c in codes)
a2 = sum(get_complexity(c, 25) for c in codes)

print_answers(a1, a2, day=21)
