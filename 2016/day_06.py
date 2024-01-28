from collections import Counter
from utils import read, print_answers

msgs = read(2016, 6).split("\n")

a1 = "".join([Counter(x).most_common()[0][0] for x in zip(*msgs)])
a2 = "".join([Counter(x).most_common()[-1][0] for x in zip(*msgs)])
print_answers(a1, a2, day=6)
