import re
from utils import read, print_answers


def is_abba(w):
    return (w[0] != w[1]) and (w[:2] == w[::-1][:2])


def has_abba(s):
    return any(is_abba(s[i : i + 4]) for i in range(len(s) - 3))


def get_abas(w):
    return [a + b + c for a, b, c in zip(w, w[1:], w[2:]) if (a == c != b)]


def invert(aba):
    return aba[1] + aba[0] + aba[1]


ips = read(2016, 7).split("\n")

a1 = a2 = 0
for s in ips:
    hypers = " ".join(re.findall(r"\[([a-z]+)\]", s))
    others = " ".join(re.sub(r"\[[a-z]+\]", " ", s).split())

    if has_abba(others) and not has_abba(hypers):
        a1 += 1

    h_abas = set(get_abas(hypers))
    o_babs = set(map(invert, get_abas(others)))
    if len(h_abas & o_babs) > 0:
        a2 += 1


print_answers(a1, a2, day=7)
