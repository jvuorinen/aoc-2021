from itertools import combinations, permutations, product, count, cycle
from functools import reduce, cache
from collections import Counter, defaultdict, deque
from math import prod
import numpy as np
from re import findall
import networkx as nx
from tqdm import tqdm

from utils import read, print_answers

# def _read(fp):
#     # print(f"Reading {fp}")
#     with open(fp) as fh:
#         result = fh.read()
#     return result


# def read(year=None, day=None):
#     if (year is None) or (day is None):
#         return _read("inputs/tmp.txt")
#     fp = f"inputs/{year}/day{day}.txt"
#     # if not os.path.exists(fp):
#     #     load_data(year, day)
#     return _read(fp)


# a,b = read().split("\n\n")
_st, _rl = read(2024, 24).split("\n\n")
start = _st.split("\n")
rules = [tuple(x.split(' -> ')) for x in _rl.split("\n")]

state = {}
for x in start:
    c, i = x.split(': ')
    state[c] = int(i)

OPS = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}
NODES = {v[1] for v in rules}
NEEDED = {n for n in NODES if n[0].startswith("z")}


#mess
_st, _rl = read(2024, 24).split("\n\n")
start = _st.split("\n")
rules = [tuple(x.split(' -> ')) for x in _rl.split("\n")]


and_xy = []
xor_xy = []
for _r in _rl.split('\n'):
    r, t = _r.split(' -> ')
    (a, op, b) = r.split(' ')
    if op == "AND" and a[0] in "xy":
        and_xy
    if op == "XOR" and a[0] in "xy":
        n = a[1:]
        _rl = _rl.replace(t, f"_xor{n}")
        if a[0] == "y":
            _rl = _rl.replace(r, " ".join([b, op, a]))

rules = [tuple(x.split(' -> ')) for x in _rl.split("\n")]
rules.sort()
rules


def get_var(state, var):
    return int("".join(map(str, [state[g] for g in sorted(state)[::-1] if g.startswith(var)])), 2)

def check(rules, state, *swaps):
    state = state.copy()
    rules = rules.copy()
    needed = NEEDED.copy()
    for a, b in swaps:
        rules[a], rules[b] = (rules[a][0], rules[b][1]), (rules[b][0], rules[a][1])
    
    fs = 0
    while needed and fs < 225:
        rule = rules.pop(0)
        a, op, b = rule[0].split(' ')
        if a in state and b in state:
            # print(rule)
            fs = 0
            # fun = f"{state[a]} {OPS[op]} {state[b]}"
            # print(x, fun)
            # state[c] = eval(fun)
            state[rule[1]] = OPS[op](state[a], state[b])
            needed -= {rule[1]}
        else:
            fs += 1
            rules.append(rule)
    if not needed:
        x = get_var(state, "x")
        y = get_var(state, "y")
        z = get_var(state, "z")
        return x, y, z

# [state["x0"+str(i)] and state["y0"+str(i)] for i in range(6)]
# [state["z0"+str(i)] for i in range(6)]



def find_affecting(node, prd, st=None):
    st = st or set()
    preds = prd.get(node, [])
    for pp in preds:
        st |= {pp}
        find_affecting(pp, prd, st)
    return st

def rules_affecting(node, rules):
    prd = {}
    for i, (r, t) in enumerate(rules):
        a, op, b = r.split(' ')
        prd[t] = {a, b}
    aff = {node} | find_affecting(node, prd)
    # res = []
    # for i, (r,t) in enumerate(rules):
    #     if ns & aff:
    #         res.append(i)
    # return res
    return set(i for i, (r, t) in enumerate(rules) if t in aff)

nodes = set(x[1] for x in rules)
RA = {n: rules_affecting(n, rules) for n in nodes}

x, y, z = check(rules,  state)
problems = bin((x+y) ^ z )[2:]
fiddled = [f"z{str(i).zfill(2)}" for i,p in enumerate(problems[::-1]) if p == '1']

stf = set.intersection(*[rules_affecting(f, rules) for f in fiddled])

pairs = [*combinations(range(len(rules)), 2)]

fun1 = rules_affecting("z23", rules)
fun2 = rules_affecting("z16", rules)

check1 = [*product(fun1, range(len(nodes)))]
check2 = [*product(fun2, range(len(nodes)))]
# to_check = [*product(fun, range(len(nodes)))]
for (a,b) in tqdm(check1):
    # x, y, z = check(rules, state, (a,b))
    # problems = bin((x+y) ^ z )[2:]
    # fiddled = [f"z{str(i).zfill(2)}" for i,p in enumerate(problems[::-1]) if p == '1']
    
    # rls = rules.copy()
    # rls[a], rls[b] = (rls[a][0], rls[b][1]), (rls[b][0], rls[a][1])
 
    # stf = set.intersection(*[rules_affecting(f, rls) for f in fiddled])
    # check2 =  [*product(stf, range(len(nodes)))]
    for (c,d) in check2:
        ch = check(rules, state, (a,b), (c,d))
        if ch:
            x, y, z = ch
            if x+y == z:
                print(rules[a], rules[b], rules[c], rules[d])
                break


for (a,b) in tqdm(check1):
    x, y, z = check(rules, state, (a,b))
    problems = bin((x+y) ^ z )[2:]
    fiddled = [f"z{str(i).zfill(2)}" for i,p in enumerate(problems[::-1]) if p == '1']
    
    rls = rules.copy()
    rls[a], rls[b] = (rls[a][0], rls[b][1]), (rls[b][0], rls[a][1])
 
    stf = set.intersection(*[rules_affecting(f, rls) for f in fiddled])
    check2 =  [*product(stf, range(len(nodes)))]
    for (c,d) in check2:
        ch = check(rules, state, (a,b), (c,d))
        if ch:
            x, y, z = ch
            if x+y == z:
                print(rules[a], rules[b], rules[c], rules[d])
                break

# for (a,b) in tqdm(pairs):
#     # x, y, z = check(rules, state, (a,b))
#     # problems = bin((x+y) ^ z )[2:]
#     # fiddled = [f"z{str(i).zfill(2)}" for i,p in enumerate(problems[::-1]) if p == '1']
    
#     # rls = rules.copy()
#     # rls[a], rls[b] = (rls[a][0], rls[b][1]), (rls[b][0], rls[a][1])
 
#     # stf = set.intersection(*[rules_affecting(f, rls) for f in fiddled])
#     # check2 =  [*product(stf, range(len(nodes)))]
#     for (c,d) in pairs:
#         ch = check(rules, state, (a,b), (c,d))
#         if ch:
#             x, y, z = ch
#             if x+y == z:
#                 print(rules[a], rules[b], rules[c], rules[d])
#                 break

check(rules, state, (0,5), (1,2))

# ff = set.union(*[find_affecting(f) for f in fiddled])

# %time check(rules, state, (1,3), (4,8))

# from random import shuffle

# shuffle(pairs)
# twopairs = [*combinations(pairs, 2)]

# t1,t2,a1 = check(rules, state)


def create_state(x, y):
    # bin(x)[2:]
    xs = {f"x{str(i).zfill(2)}": int(n) for i, n in enumerate(bin(x)[2:][::-1])}
    ys = {f"y{str(i).zfill(2)}": int(n) for i, n in enumerate(bin(y)[2:][::-1])}
    return xs | ys

st = {k: 0 for k in state} |  create_state(11, 13)

check(rules, st)


def count_correct(x, y, z):
    return bin(~((x+y) ^ z)).count('1')

# rules

res = {}
for (a, b) in tqdm(pairs):
    ch = check(rules, state, (a,b))
    if ch:
        x, y, z = ch
        res[(a, b)] = count_correct(x, y, z)

# x, y, z = check(rules, state, (173, 208))

# count_correct(x, y, z)

# b1 = bin(x+y)[2:]
# b2 = bin(z)[3:]

# sum([a==b for a, b in zip(b1, b2)])

sp = [sorted(res, key=res.get)[::-1]][0]
for (a, b) in tqdm(sp):
    for (c,d) in pairs:
        ch = check(rules, state, (a,b), (c,d))
        if ch:
            x, y, z = ch
            if x+y == z:
                print(rules[a], rules[b], rules[c], rules[d])


# for (a,b), (c,d) in tqdm(twopairs):
#     rls = rules.copy()
#     rls[b], rls[a] = rls[b][:-6] + rls[a][-6:], rls[a][:-6] + rls[b][-6:]
#     rls[d], rls[c] = rls[d][:-6] + rls[c][-6:], rls[c][:-6] + rls[d][-6:]
#     x, y, z = check(rls)
#     if x+y == z:
#         print(rls[a][-3:], rls[b][-3:], rls[c][-3:], rls[d][-3:])

# candidates = [*combinations(pairs, 4)]
# len(candidates)

# pairs = [*combinations(rules, 4)]
# for pair in pairs:
#     break

# %prun _,_,a1 = check(rules)
a2 = None

print_answers(a1, a2, day=24)
