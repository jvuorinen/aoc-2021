from collections import defaultdict
from utils import read, print_answers


def parse(raw):
    a, *bs = raw.split("\n\n")
    state = a.split("\n")[0][-2]
    steps = int(a.split("\n")[1].split()[-2])

    ops = {}
    for b in bs:
        lines = b.split("\n")
        ops[lines[0][-2]] = [
            (int(lines[2][-2]), (-1, 1)["right" in lines[3]], lines[4][-2]),
            (int(lines[6][-2]), (-1, 1)["right" in lines[7]], lines[8][-2]),
        ]
    return state, steps, ops


raw = read(2017, 25)
state, steps, ops = parse(raw)

mem = defaultdict(int)
i = 0
for _ in range(steps):
    w, d, state = ops[state][mem[i]]
    mem[i] = w
    i += d

a1 = sum(v == 1 for v in mem.values())
print_answers(a1, None, day=25)
