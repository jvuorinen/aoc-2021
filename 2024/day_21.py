from functools import cache
from utils import read, print_answers


NUM = {x: c - 1j * r for r, line in enumerate(["789","456", "123", "x0A"]) for c, x in enumerate(line) if x != "x"}
DIR = {x: c - 1j * r for r, line in enumerate(["x^A", "<v>"]) for c, x in enumerate(line) if x != "x"}
D = {-1: "<", 1: ">", 1j: "^", -1j: "v"}


def magnitude_and_dir(n):
    return abs(n), n // abs(n) if n else 0


def get_paths(pad, fr, to):
    d = pad[to] - pad[fr]
    rm, rd = magnitude_and_dir(int(d.real))
    im, id = magnitude_and_dir(int(d.imag))
    seq = [rd] * rm + [1j * id] * im
    paths = set()
    for ds in (seq, seq[::-1]):
        tst = pad[fr]
        if all((tst := tst + dd) in pad.values() for dd in ds):
            paths.add("".join(map(D.get, ds)) + "A")
    return paths


@cache
def shortest(seq, depth):
    pad = DIR if any(ch in seq for ch in "<>^v") else NUM
    aseq = "A" + seq
    possible = [get_paths(pad, fr, to) for fr, to in zip(aseq[:-1], aseq[1:])]
    if depth == 0:
        return sum(min(map(len, s)) for s in possible)
    return sum(min(shortest(x, depth - 1) for x in s) for s in possible)


def get_complexity(code, depth):
    return int(code[:-1]) * shortest(code, depth)


codes = read(2024, 21).split("\n")

a1 = sum(get_complexity(c, 2) for c in codes)
a2 = sum(get_complexity(c, 25) for c in codes)

print_answers(a1, a2, day=21)
