from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm
from utils import read, print_answers

# a,b = read().split("\n\n")
a, b = read(2024, 24).split("\n\n")
start = a.split("\n")
rules = b.split("\n")

state = defaultdict()
for x in start:
    c, i = x.split(': ')
    state[c] = int(i)

OPS = {
    "AND": "&",
    "OR": "|",
    "XOR": "^"
}

while rules:
    # print(rules)
    x = rules.pop(0)
    a, op, b, c = findall("(...) (AND|OR|XOR) (...) -> (...)", x)[0]
    if a in state and b in state:
        fun = f"{state[a]} {OPS[op]} {state[b]}"
        print(x, fun)
        state[c] = eval(fun)
    else:
        rules.append(x)

a1 = int("".join(map(str, [state[x] for x in sorted(state)[::-1] if x.startswith("z")])), 2)
a2 = None

print_answers(a1, a2, day=24)
