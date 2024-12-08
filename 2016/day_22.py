from itertools import combinations, permutations, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from dataclasses import dataclass
from utils import read, print_answers


@dataclass
class Node:
    name: str
    size: int
    used: int
    av: int
    pct: int

    def __hash__(self):
        return hash(self.name)

lines = read(2016, 22).split("\n")

nodes = []
for line in lines[2:]:
    name = line.split(' ')[0]
    size, used, av, pct = map(int, findall(r" (\d+)", line))
    nodes.append(Node(name, size, used, av, pct))

good = set([
    (a, b) for a, b in permutations(nodes, 2)
    if a.used > 0 and a.used <= b.av])

a1 = None
a2 = None

print_answers(a1, a2, day=22)
