from collections import defaultdict
from utils import read, print_answers

raw = read(2017, 22).split("\n")

states = defaultdict(lambda: "C")
for r, line in enumerate(raw):
    for c, x in enumerate(line):
        states[c + r * 1j] = "I" if x == "#" else "C"


def simulate(turn, mod, n, states):
    states = states.copy()
    loc = [*states][-1] / 2
    hdg = -1j
    res = 0
    for _ in range(n):
        hdg *= turn[states[loc]]
        states[loc] = mod[states[loc]]
        if states[loc] == "I":
            res += 1
        loc += hdg
    return res


a1 = simulate({"I": 1j, "C": -1j}, {"I": "C", "C": "I"}, 10_000, states)
a2 = simulate(
    {"C": -1j, "W": 1, "I": 1j, "F": -1},
    {"C": "W", "W": "I", "I": "F", "F": "C"},
    10_000_000,
    states,
)

print_answers(a1, a2, day=22)  # 5433 2512599
