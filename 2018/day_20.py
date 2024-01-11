import networkx as nx
from utils import read, print_answers

path = read("inputs/day_20b.txt")[1:-1]

G = nx.Graph()
loc = 0j
stack = []
for c in path:
    match c:
        case "(":
            stack.append(loc)
        case "|":
            loc = stack[-1]
        case ")":
            loc = stack.pop()
        case _:
            _loc = loc + {"N": -1j, "S": 1j, "W": -1, "E": 1}[c]
            G.add_edge(loc, _loc)
            loc = _loc

paths = nx.algorithms.shortest_path_length(G, 0)

a1 = max(paths.values()) - 1
a2 = sum([x >= 1000 for x in paths.values()])
print_answers(a1, a2, day=20)  # 3871 8600
