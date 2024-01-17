from utils import read, print_answers

raw = read(2017, 19).split("\n")
M = {j + i * 1j: c for i, row in enumerate(raw) for j, c in enumerate(row) if c != " "}


def get_next(loc, hdg):
    for _hdg in (hdg, hdg * 1j, hdg * -1j):
        if (_loc := loc + _hdg) in M:
            return _loc, _hdg


loc = raw[0].index("|")
hdg = 1j

a1 = 1
a2 = ""
while nxt := get_next(loc, hdg):
    a1 += 1
    loc, hdg = nxt
    if (c := M[loc]).isalpha():
        a2 += c

print_answers(a1, a2, day=19)
