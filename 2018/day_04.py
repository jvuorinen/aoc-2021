import re
from collections import defaultdict
import numpy as np
from utils import print_answers, read


def load():
    raw_in = read("inputs/day_04b.txt").split("\n")

    asleep = defaultdict(lambda: np.zeros(60, int))
    for r in sorted(raw_in):
        ts, e = re.findall(r"\[(.+)\] (.+)", r)[0]
        minute = int(re.findall(r":(..)", ts)[0])
        match e.split():
            case "Guard", _g, *_:
                g = int(_g[1:])
            case "falls", "asleep":
                start = minute
            case "wakes", "up":
                asleep[g][start:minute] += 1
    return asleep


asleep = load()

tgt_1 = max(asleep, key=lambda x: asleep[x].sum())
tgt_2 = max(asleep, key=lambda x: asleep[x].max())

a1 = tgt_1 * asleep[tgt_1].argmax()
a2 = tgt_2 * asleep[tgt_2].argmax()
print_answers(a1, a2, day=4)
