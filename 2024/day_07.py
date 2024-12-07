from itertools import product
from utils import read, print_answers


def _apply(val, op, x):
    match op:
        case "|":
            return int(f"{val}{x}")
        case "+":
            return val + x
        case "*":
            return val * x


def check(line, ops):
    _exp, _ns = line.split(": ")
    exp = int(_exp)
    ns = [int(x) for x in _ns.split(" ")]

    for cmb in product(*[list(ops)] * (len(ns) - 1)):
        val, rest = ns[0], ns[1:]
        for op in cmb:
            val = _apply(val, op, rest.pop(0))
        if val == exp:
            return exp
    return 0


lines = read(2024, 7).split("\n")

a1 = sum(check(x, "*+") for x in lines)
a2 = sum(check(x, "*+") or check(x, "*|+") for x in lines)

print_answers(a1, a2, day=7)
