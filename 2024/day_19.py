from functools import cache
from utils import read, print_answers


_p, _m = read(2024, 19).split("\n\n")
pats = _p.split(", ")
mats = _m.split("\n")


@cache
def count(m):
    return 1 if not m else sum(count(m[len(p) :]) for p in pats if m.startswith(p))


nways = [count(m) for m in mats]
print_answers(sum(x > 0 for x in nways), sum(nways), day=19)
