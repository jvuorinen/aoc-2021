from utils import read, print_answers


def _apply(val, op, x):
    match op:
        case "|":
            return int(f"{val}{x}")
        case "+":
            return val + x
        case "*":
            return val * x


def backtrack(val, exp, ns, ops):
    if val > exp:
        return
    if not ns:
        return val if (val == exp) else None
    for op in ops:
        _n, _ns = ns[0], ns[1:]
        _val = _apply(val, op, _n)
        if res := backtrack(_val, exp, _ns, ops):
            return res


def check(line, ops):
    _exp, _ns = line.split(": ")
    exp = int(_exp)
    ns = [int(x) for x in _ns.split(" ")]
    first, rest = ns[0], ns[1:]
    return backtrack(first, exp, rest, ops) or 0


lines = read(2024, 7).split("\n")

a1 = sum(check(x, "*+") for x in lines)
a2 = sum(check(x, "*+") or check(x, "*|+") for x in lines)

print_answers(a1, a2, day=7)
