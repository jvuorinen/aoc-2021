from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm
from utils import read, print_answers

a, b = read().split("\n\n")
# a, b = read(2024, 15).split("\n\n")


a = a.replace("#", "##")
a = a.replace("O", "[]")
a = a.replace(".", "..")
a = a.replace("@", "@.")

M = {c + 1j * r: x for r, line in enumerate(a.split('\n')) for c, x in enumerate(line)}
W, H = int(max(x.real for x in M)) + 1, int(max(x.imag for x in M)) + 1

dirs = [{'<': -1, '>': 1, '^': -1j, 'v': 1j}[x] for x in b.replace("\n", "")]


p = next(k for k, v in M.items() if v == '@')
barrels = set([k for k, v in M.items() if v == '['])
floor = set([k for k, v in M.items() if v != '#'])

def draw():
    area = [list('#'* W) for _ in range(H)]
    for z in floor:
        area[int(z.imag)][int(z.real)] = '.'
    for z in barrels:
        area[int(z.imag)][int(z.real)] = '['
        area[int((z+1).imag)][int((z+1).real)] = ']'
    area[int(p.imag)][int(p.real)]= '@'
    print("\n".join(map("".join, area)))
    print()

def get_stack(p, d, stack):
    if p - 1 in barrels:
        # print("apply p correction")
        p -= 1
    if p not in barrels:
        return
    # print("Checking ", p)
    _p = p + d
    if (_p not in floor) or (_p + 1 not in floor):
        # print(_p, " blocked")
        stack.clear()
        return
    # print(p, " is free")
    stack.add(p)
    if d in (1, -1):
        if _p + d in barrels:
            get_stack(_p + d, d, stack)
    else:
        if _p - 1 in barrels:
            get_stack(_p - 1, d, stack)
        if _p in barrels:
            get_stack(_p, d, stack)
        if _p + 1 in barrels:
            get_stack(_p + 1, d, stack)
    # print(stack)
    return stack or None

# draw()
# get_stack(p, 1, set())
# draw()

while dirs:
    d = dirs.pop(0)
    if p + d in floor and (p+d) not in barrels and (p+d-1) not in barrels:
        # print("FREE MOVE")
        p += d
    else:
        stack = get_stack(p+d, d, set())
        if stack:
            # draw()
            # print({-1: "<", 1: ">", -1j: "^", 1j: "v"}[d])
            barrels -= stack
            barrels |= {b + d for b in stack}
            p += d
            # draw()
            # break
    # if p == 6 + 6j:
    #     print(len(dirs))
    #     break
# draw()


a1 = int(sum([100*z.imag + z.real for z in barrels]))
a2 = None

print_answers(a1, a2, day=15)
# 1426855
# 1419441 high