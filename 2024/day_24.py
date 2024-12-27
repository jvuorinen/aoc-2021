from itertools import combinations
from utils import read, print_answers


_st, _rl = read(2024, 24).split("\n\n")
state = {}
for x in _st.split("\n"):
    c, i = x.split(": ")
    state[c] = int(i)
rules = []
for x in _rl.split("\n"):
    r, t = x.split(" -> ")
    rules.append((r.split(" "), t))


OPS = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}


def get_var(state, var):
    return int("".join(str(state.get(var + str(i).zfill(2), 0)) for i in range(50))[::-1], 2)


def run(rules, state, *swaps):
    state = state.copy()
    rules = rules.copy()
    for a, b in swaps:
        rules[a], rules[b] = (rules[a][0], rules[b][1]), (rules[b][0], rules[a][1])

    fs = 0
    while rules and fs < 225:
        rule = rules.pop(0)
        (a, op, b), t = rule
        if a in state and b in state:
            fs = 0
            state[t] = OPS[op](state[a], state[b])
        else:
            fs += 1
            rules.append(rule)
    x = get_var(state, "x")
    y = get_var(state, "y")
    z = get_var(state, "z")
    return x, y, z


def rule_type(a, op, b):
    if op == "OR":
        return "n or n"
    if op == "XOR":
        return "x xor y" if a[0] in "xy" else "n xor n"
    return "x and y" if a[0] in "xy" else "n and n"


def is_problem(r, t):
    correct = {
        "x xor y": {"n and n", "n xor n"},
        "n or n": {"n and n", "n xor n"},
        "n and n": {"n or n"},
        "x and y": {"n or n"},
        "n xor n": "out",
    }
    rt = rule_type(*r)
    tt = "out" if t[0] == "z" else {rule_type(*r) for r, _ in rules if t in r}
    return tt != correct[rt]


def fix(rules, state):
    candidates = [i for i, (r, t) in enumerate(rules) if is_problem(r, t)]
    for swaps in combinations(combinations(candidates, 2), 4):
        if res := run(rules, state, *swaps):
            x, y, z = res
            if x + y == z:
                return ",".join(sorted([rules[x][1] for sw in swaps for x in sw]))


_, _, a1 = run(rules, state)
a2 = fix(rules, state)

print_answers(a1, a2, day=24)
