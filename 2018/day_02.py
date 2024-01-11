from collections import Counter
from itertools import combinations
from utils import read, print_answers

boxes = read("inputs/day_02.txt").split()


def p1(boxes):
    occ = [set(Counter(b).values()) for b in boxes]
    return sum([2 in x for x in occ]) * sum([3 in x for x in occ])


def p2(boxes):
    for b1, b2 in combinations(boxes, 2):
        matches = [c1 == c2 for c1, c2 in zip(b1, b2)]
        if sum(matches) == len(b1) - 1:
            return "".join([c for c, m in zip(b1, matches) if m])


a1 = p1(boxes)
a2 = p2(boxes)
print_answers(a1, a2, day=2)
