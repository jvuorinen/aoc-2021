from utils import read, print_answers

a1 = a2 = 0
for line in read(2015, 2).split("\n"):
    a, b, c = map(int, line.split("x"))
    facets = a * b, b * c, c * a
    a1 += min(facets) + sum(facets) * 2
    a2 += 2 * sum(sorted([a, b, c])[:2]) + (a * b * c)

print_answers(a1, a2, day=2)
