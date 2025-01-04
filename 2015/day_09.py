from utils import read, print_answers


def travel(a, todo, res, ln=0):
    if not todo:
        res.add(ln)
    for b in todo:
        travel(b, todo - {b}, res, ln + D[a, b])
    return res


D = {}
for line in read(2015, 9).split("\n"):
    a, _, b, _, n = line.split(" ")
    D[a, b] = D[b, a] = int(n)

nodes = set.union(*map(set, D))
routes = set.union(*[travel(n, nodes - {n}, set()) for n in nodes])

print_answers(min(routes), max(routes), day=9)
