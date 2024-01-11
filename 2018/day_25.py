import networkx as nx
from itertools import combinations
from utils import read, print_answers


def manhattan(a, b):
    return sum([abs(c1 - c2) for c1, c2 in zip(a, b)])


points = [tuple([*map(int, line.split(","))]) for line in read("inputs/day_25a.txt").split("\n")]

G = nx.Graph()
for p in points:
    G.add_edge(p, p)

for p1, p2 in combinations(points, 2):
    if (d := manhattan(p1, p2)) <= 3:
        G.add_edge(p1, p2)

a1 = nx.number_connected_components(G)
print_answers(a1, None, day=25)
