import re

from utils import print_answers, read_file

SIZE = 256


def hash(txt):
    x = 0
    for c in txt:
        x += ord(c)
        x *= 17
        x %= SIZE
    return x


def parse_lens(w):
    lb, op, _f = re.findall(r"([a-z]+)([=-])(\d*)", w)[0]
    f = int(_f) if _f else None
    return lb, op, f


def solve_2(lenses):
    boxes = [[] for _ in range(SIZE)]
    for lens in lenses:
        lb, op, _ = lens
        h = hash(lb)
        if op == "=":
            for i, old in enumerate(boxes[h]):
                if old[0] == lb:
                    boxes[h][i] = lens
                    break
            else:
                boxes[h].append(lens)
        else:
            boxes[h] = [old for old in boxes[h] if old[0] != lb]

    res = sum([i * j * lens[-1] for i, b in enumerate(boxes, 1) for j, lens in enumerate(b, 1)])
    return res


words = read_file("inputs/day_15b.txt").split(",")
lenses = [parse_lens(x) for x in words]

a1 = sum([hash(w) for w in words])
a2 = solve_2(lenses)

print_answers(a1, a2, day=15)  # Correct: 515495, 229349
