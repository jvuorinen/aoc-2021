from collections import Counter
from utils import read, print_answers

msgs = read(2016, 6).split("\n")
counted = [Counter(x).most_common() for x in zip(*msgs)]

a1 = "".join([c[0][0] for c in counted])
a2 = "".join([c[-1][0] for c in counted])

print_answers(a1, a2, day=6)
