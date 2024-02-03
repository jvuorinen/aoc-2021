from collections import defaultdict
import re
from utils import read, print_answers

raw = read(2016, 10).split("\n")

bins = defaultdict(list)
targets = {}
for line in raw:
    spl = line.split(" ")
    if line.startswith("value"):
        c, b = re.findall(r"value (\d+) goes to (bot \d+)", line)[0]
        bins[b].append(int(c))
    else:
        fr, t1, t2 = re.findall(r"(?:bot|output) \d+", line)
        targets[fr] = (t1, t2)

todo = [k for k, v in bins.items() if len(v) == 2]
while todo:
    b = todo.pop(0)
    chips = sorted(bins[b])
    if chips == (17, 61):
        a1 = b.split(" ")[-1]
    for c, t in zip(chips, targets[b]):
        bins[t].append(c)
        if len(bins[t]) > 1:
            todo.append(t)
    bins[b] = []

a2 = bins["output 0"][0] * bins["output 1"][0] * bins["output 2"][0]
print_answers(a1, a2, day=10)  # 113 12803
