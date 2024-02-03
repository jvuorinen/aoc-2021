from collections import defaultdict
from math import prod
from utils import read, print_answers

raw = read(2016, 10).split("\n")

holdings = defaultdict(list)
targets = {}
for line in raw:
    spl = line.split(" ")
    if spl[0] == "value":
        c, b = int(spl[1]), " ".join(spl[-2:])
        holdings[b].append(c)
        if len(holdings[b]) == 2:
            todo = [b]
    else:
        fr = " ".join(spl[0:2])
        t1 = " ".join(spl[5:7])
        t2 = " ".join(spl[10:12])
        targets[fr] = (t1, t2)

while todo:
    b = todo.pop(0)
    chips = sorted(holdings[b])
    if chips == (17, 61):
        a1 = b.split(" ")[-1]
    for c, t in zip(chips, targets[b]):
        holdings[t].append(c)
        if len(holdings[t]) > 1:
            todo.append(t)
    holdings[b] = []

a2 = prod([holdings[f"output {x}"][0] for x in (0, 1, 2)])

print_answers(a1, a2, day=10)  # 113 12803
