from functools import cache
from utils import read, print_answers


_p, _m = read(2024, 19).split("\n\n")
pats = _p.split(", ")
mats = _m.split("\n")


@cache
def count(mat):
    if not mat:
        return 1
    return sum(count(mat[len(p) :]) for p in pats if mat.startswith(p))


nways = [count(m) for m in mats]
print_answers(sum(x > 0 for x in nways), sum(nways), day=19)
