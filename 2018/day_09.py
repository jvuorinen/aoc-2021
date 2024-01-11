import re
from dataclasses import dataclass
from typing import Any
from utils import read, print_answers


@dataclass
class Marble:
    value: int
    prev: Any = None
    next: Any = None


def insert(i: int, m: Marble):
    new = Marble(i)
    new.prev = m
    new.next = m.next
    new.prev.next = new.next.prev = new
    return new


def remove(m: Marble):
    m.prev.next = m.next
    m.next.prev = m.prev
    return m.next


def solve(players, limit):
    m = Marble(0)
    m.next = m.prev = m
    p = 0
    scores = [0 for _ in range(players)]
    for i in range(1, limit + 1):
        if i % 23 != 0:
            m = insert(i, m.next)
        else:
            for _ in range(7):
                m = m.prev
            scores[p] += m.value + i
            m = remove(m)
        p = (p + 1) % players
    return max(scores)


players, limit = map(int, re.findall(r"\d+", read("inputs/day_09.txt")))

a1 = solve(players, limit)
a2 = solve(players, limit * 100)
print_answers(a1, a2, day=9)
