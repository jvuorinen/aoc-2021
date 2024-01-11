from utils import read, print_answers

ns = [*map(int, read(2017, 1))]
ln = len(ns)

a1 = sum([n for i, n in enumerate(ns) if n == ns[(i + 1) % ln]])
a2 = sum([n for i, n in enumerate(ns) if n == ns[(i + ln // 2) % ln]])

print_answers(a1, a2, day=1)  # 1119 1420
