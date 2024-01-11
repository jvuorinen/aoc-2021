from string import ascii_lowercase
from utils import print_answers, read


def opposed(a, b):
    return (a != b) and (a.lower() == b.lower())


def react(poly):
    res = []
    for c in poly:
        if res and opposed(res[-1], c):
            res.pop(-1)
        else:
            res.append(c)
    return res


def remove(poly, unit):
    return [c for c in poly if c.lower() != unit]


poly = list(read("inputs/day_05b.txt"))
reacted = react(poly)

a1 = len(reacted)
a2 = min([len(react(remove(reacted, c))) for c in ascii_lowercase])
print_answers(a1, a2, day=5)
