from functools import cache
from utils import read, print_answers


_p, _m = read(2024, 19).split("\n\n")
pats = _p.split(", ")
mats = _m.split("\n")


@cache
def matches(mat, s=0):
    if len(mat) == 0:
        return 1
    for p in [p for p in pats if mat.startswith(p)]:
        s += matches(mat[len(p) :])
    return s


nways = [matches(m) for m in mats]

a1 = sum(x > 0 for x in nways)
a2 = sum(nways)

print_answers(a1, a2, day=19)
