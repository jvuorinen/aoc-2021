from itertools import combinations, permutations, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from utils import read, print_answers

lines = read().split("\n")
# lines = read(2016, 21).split("\n")

original = 'abcdefgh'
# original = "abcde"

NROT = {i: (-(i + 1 + int(i >= 4)) % len(original)) for i in range(len(original))}
# INVROT = {k: v for k, v in NROT.items()}

def fumble(lst, line):
    lst = lst.copy()
    if "swap position" in line:
        a, b = map(int, findall(r"\d", line))
        lst[a], lst[b] = lst[b], lst[a]
    elif "swap letter" in line:
        a, b = findall(r"letter (.)", line)
        ia, ib = lst.index(a), lst.index(b)
        lst[ia], lst[ib] = lst[ib], lst[ia]
    elif "reverse" in line:
        a, b = map(int, findall(r"\d", line))
        lst[a:b+1] = lst[a:b+1][::-1]
    elif "move" in line:
        a, b = map(int, findall(r"\d", line))
        # if invert:
        #     a, b = b, a
        lst.insert(b, lst.pop(a))
    elif "rotate" in line:
        if "based" in line:
            a = findall(r"letter (.)", line)[0]
            ia = lst.index(a)
            n = NROT[ia]
        else:
            n = int(findall(r"(.) step", line)[0])
            if "right" in line:
                n *= -1
            # if invert:
            #     n *= -1
            n %= len(lst)
        lst = lst[n:] + lst[:n]
    return lst

invert = False
"".join(reduce(fumble, lines, list(original)))

invert = True
"".join(reduce(fumble, lines, list(original)))

a1 = "".join(reduce(fumble, lines, list(original)))

# a2 = "".join(["fbgdceah"[i] for i in ixs])

# print_answers(a1, a2, day=21)
