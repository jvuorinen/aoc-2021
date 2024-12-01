import re
from utils import print_answers, read

raw = read(2024, 1)

ints = [int(x) for x in re.findall(r"\d+", raw)]
g1 = ints[::2]
g2 = ints[1::2]

a1 = sum([abs(a - b) for a, b in zip(sorted(g1), sorted(g2))])
a2 = sum([a * g2.count(a) for a in g1])

print_answers(a1, a2, day=1)
