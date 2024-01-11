import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional
from itertools import count
from utils import read, print_answers


@dataclass
class Worker:
    t: int = 0
    task: Optional[str] = None


def solve(fw, bw, n_elves, timefun):
    req = {a: set(b) for a, b in bw.items()}
    workers = [Worker() for _ in range(n_elves)]
    opened = ""
    can_open = list(set(fw) - set(req))

    for t in count():
        for w in workers:
            w.t = max(0, w.t - 1)

        available = [w for w in workers if w.t == 0]
        for w in available:
            if w.task is not None:
                opened += w.task
                if len(opened) == len(fw) + 1:
                    return opened, t
                for b in fw[w.task]:
                    req[b].remove(w.task)
                    if not req[b] and b not in opened:
                        can_open.append(b)
                w.task = None

        can_open.sort()
        while available and can_open:
            w, task = available.pop(0), can_open.pop(0)
            w.task = task
            w.t = timefun(w.task)


raw_in = read("inputs/day_07b.txt")
fw, bw = defaultdict(list), defaultdict(list)
for a, b in re.findall(r"Step (.) .* step (.)", raw_in):
    fw[a].append(b)
    bw[b].append(a)

a1, _ = solve(fw, bw, 1, (lambda x: 1))
_, a2 = solve(fw, bw, 5, (lambda x: ord(x) - ord("A") + 61))
print_answers(a1, a2, day=7)
