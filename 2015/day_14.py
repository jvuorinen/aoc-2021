from collections import Counter
import re
from utils import read, print_answers

stats = [[*map(int, re.findall(r"\d+", line))] for line in read(2015, 14).split("\n")]


def score(v, p, w, time):
    d, m = divmod(time, p + w)
    return v * (p * d + min(m, p))


def argmax(lst):
    return [i for i, x in enumerate(lst) if x == max(lst)]


a1 = max(score(v, p, w, 2503) for v, p, w in stats)

leaders = [argmax([score(v, p, w, t) for v, p, w in stats]) for t in range(1, 2503)]
a2 = max(Counter([x for lst in leaders for x in lst]).values())

print_answers(a1, a2, day=14)
