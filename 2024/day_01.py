import re
from utils import print_answers, read

raw = read(2024, 1)

g1, g2 = map(
    lambda lst: [int(x) for x in lst],
    zip(*re.findall(r"(\d+)   (\d+)", raw)))

a1 = sum([abs(a - b) for a, b in zip(sorted(g1), sorted(g2))])
a2 = sum([a * g2.count(a) for a in g1])

print_answers(a1, a2, day=1)
