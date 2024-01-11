import re

from utils import print_answers, read_file


def parse(x):
    res = re.findall("(....) (.) (....)", x)
    return res[0] if res else int(x)


def assemble_eq(m, monkeys):
    if m == "humn":
        return "x"
    match parse(monkeys[m]):
        case int(a):
            return a
        case a, op, b:
            aa = assemble_eq(a, monkeys)
            bb = assemble_eq(b, monkeys)
            if m == "root":
                if "x" not in aa:
                    aa, bb = bb, aa
                return aa, bb
            else:
                eq = f"({aa}) {op} ({bb})"
                return eq


def _split_eq(eq):
    t = 0
    for i, c in enumerate(eq):
        if c == "(":
            t += 1
        elif c == ")":
            t -= 1
        if t == 0:
            return eq[1:i], eq[i + 2 : i + 3], eq[i + 5 : -1]


def solve_eq(left, right):
    right = eval(right) if isinstance(right, str) else right

    if left == "x":
        return int(right)

    a, op, b = _split_eq(left)
    xleft = "x" in a

    left = a if xleft else b
    match op:
        case "/":
            right = (right * eval(b)) if xleft else eval(a) // right
        case "*":
            right = (right // eval(b)) if xleft else (right // eval(a))
        case "+":
            right = (right - eval(b)) if xleft else (right - eval(a))
        case "-":
            right = (right + eval(b)) if xleft else (eval(a) - right)

    return solve_eq(left, right)


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_21b.txt").split("\n")
    monkeys = dict([x.split(": ") for x in raw_in])

    left, right = assemble_eq("root", monkeys)

    a1 = int(eval(f"{left} + {right}".replace("x", monkeys["humn"])))
    a2 = solve_eq(left, right)

    print_answers(a1, a2, day=21)
    # 331120084396440
    # 3378273370680
