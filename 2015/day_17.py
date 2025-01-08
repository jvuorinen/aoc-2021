from collections import Counter
from utils import read, print_answers


def knapsack(chosen, todo, coll):
    s = sum(chosen)
    if s == 150:
        coll.append(chosen)
    if todo and s < 150:
        first, rest = todo[0], todo[1:]
        knapsack(chosen, rest, coll)
        knapsack(chosen + [first], rest, coll)
    return coll


sizes = sorted(int(x) for x in read(2015, 17).split("\n"))
solutions = knapsack([], sizes, [])
counts = Counter(map(len, solutions))

a1 = sum(counts.values())
a2 = counts[min(counts)]
print_answers(a1, a2, day=17)
