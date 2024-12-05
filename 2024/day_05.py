from functools import cmp_to_key
from collections import defaultdict
from utils import read, print_answers

raw = read(2024, 5)
_rules, _updates = raw.split("\n\n")

rules = defaultdict(int)
for _rule in _rules.split("\n"):
    x, y = _rule.split("|")
    rules[(x, y)] = -1
    rules[(y, x)] = 1

a1 = 0
a2 = 0
for _upd in _updates.split("\n"):
    upd = _upd.split(",")
    srt = sorted(upd, key=cmp_to_key(lambda x, y: rules[(x, y)]))
    if srt == upd:
        a1 += int(srt[len(srt) // 2])
    else:
        a2 += int(srt[len(srt) // 2])


print_answers(a1, a2, day=5)
