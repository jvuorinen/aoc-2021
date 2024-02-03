from collections import defaultdict
from math import prod
import re
from utils import read, print_answers

raw = read(2016, 10).split("\n")

holdings = defaultdict(list)
targets = {}
for line in raw:
    spl = line.split(" ")
    if line.startswith("value"):
        c, b = re.findall(r"value (\d+) goes to (bot \d+)", line)[0]
        holdings[b].append(int(c))
    else:
        fr, t1, t2 = re.findall(r"(?:bot|output) \d+", line)
        targets[fr] = (t1, t2)

todo = [k for k, v in holdings.items() if len(v) == 2]
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
