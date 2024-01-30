import re
from utils import read, print_answers


def is_abba(w):
    return (w[0] != w[1]) and (w[:2] == w[::-1][:2])


def has_abba(s):
    return any(is_abba(s[i : i + 4]) for i in range(len(s) - 3))


def is_aba(w):
    return w[0] == w[2] != w[1]


def get_abas(w):
    return [chk for i in range(len(w) - 2) if is_aba(chk := w[i : i + 3])]


def invert(aba):
    return aba[1] + aba[0] + aba[1]


ips = read(2016, 7).split("\n")

a1 = a2 = 0
for s in ips:
    hypers = re.findall(r"\[([a-z]+)\]", s)
    others = re.sub(r"\[[a-z]+\]", " ", s).split()

    if not any(map(has_abba, hypers)) and any(map(has_abba, others)):
        a1 += 1

    h_abas = set.union(*[set(get_abas(x)) for x in hypers])
    o_babs = set.union(*[set(map(invert, get_abas(x))) for x in others])
    if len(h_abas & o_babs) > 0:
        a2 += 1


print_answers(a1, a2, day=7)
