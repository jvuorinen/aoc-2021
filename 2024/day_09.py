from itertools import chain
from functools import reduce
from utils import read, print_answers

raw = read(2024, 9)

files = [int(c)*[i] for i, c in enumerate(raw[::2])]
space = [int(c)*[None] for i, c in enumerate(raw[1::2])]

original = reduce(list.__add__, [*chain(*zip(files, space + [[None]]))])

# Part 1
data = original.copy()

i, ii = 0, len(data) - 1
while True:
    while data[i] is not None:
        i += 1
    while data[ii] is None:
        ii -= 1
    if ii <= i:
        break
    data[i], data[ii] = data[ii], data[i]

a1 = sum(i*(x or 0) for i, x in enumerate(data))

# Part 2
data = original.copy()
ixs = [data.index(i) for i in range(len(files))]
empty = [(i + len(f), ii-(i + len(f))) for i, ii, f in zip(ixs, ixs[1:], files)]
empty = [(i, s) for i, s in empty if s]

for ii, f in zip(ixs[::-1], files[::-1]):
    s = len(f)
    for j, (i, es) in enumerate(empty):
        if i >= ii:
            break
        if es < s:
            continue
        data[i:i+s] = f
        data[ii:ii+s] = [None] * s
        empty.pop(j)
        if (ns := es - s):
            empty.insert(j, (i+s, ns))
        break

a2 = sum(i*(x or 0) for i, x in enumerate(data))


print_answers(a1, a2, day=9)
# 6430446922192
# 6460170593016
