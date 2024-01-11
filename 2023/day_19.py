import re
from math import prod
from utils import read_file, print_answers


def parse(raw_in):
    _f, _p = raw_in.split("\n\n")

    flows = {}
    for f in _f.split():
        a, b = f[:-1].split("{")
        flows[a] = b.split(",")

    parts = [[*map(int, re.findall("\d+", p))] for p in _p.split()]
    return parts, flows


def resolve(p, flows, f="in"):
    if f in "RA":
        return "RA".find(f)
    x, m, a, s = p
    for step in flows[f]:
        if ":" not in step:
            return resolve(p, flows, step)
        expr, _f = step.split(":")
        if eval(expr):
            return resolve(p, flows, _f)


def reverse(expr):
    if ">" in expr:
        var, n = expr.split(">")
        return f"{var}<{int(n)+1}"
    else:
        var, n = expr.split("<")
        return f"{var}>{int(n)-1}"


def bind(bindings, expr):
    var, op, n = re.findall(r"([a-z]+)([<>])(\d+)", expr)[0]

    _b = list(map(list, bindings))
    if op == ">":
        _b["xmas".index(var)][0] = int(n) + 1
    else:
        _b["xmas".index(var)][1] = int(n)
    return tuple(map(tuple, _b))


def count(f, flows, bindings=None):
    if not bindings:
        bindings = tuple((1, 4001) for _ in range(4))
    if f in "AR":
        return prod(b - a for a, b in bindings) if f == "A" else 0
    todo = flows[f][:]
    c = 0
    while todo:
        step = todo.pop(0)
        if ":" not in step:
            c += count(step, flows, bindings)
        else:
            expr, _f = step.split(":")
            _b = bind(bindings, expr)
            c += count(_f, flows, _b)
            bindings = bind(bindings, reverse(expr))
    return c


raw_in = read_file("inputs/day_19b.txt")
parts, flows = parse(raw_in)

a1 = sum([resolve(p, flows) * sum(p) for p in parts])
a2 = count("in", flows)

print_answers(a1, a2, day=19)  # Correct: 420739, 130251901420382
