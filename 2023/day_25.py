import networkx as nx
from utils import read_file, print_answers

raw_in = read_file("inputs/day_25b.txt")

g = nx.Graph()
for line in raw_in.split("\n"):
    a, bs = line.split(": ")
    for b in bs.split():
        g.add_edge(a, b)
        g.add_edge(b, a)

bc = nx.edge_betweenness_centrality(g)
cuts = sorted(bc, key=bc.get)[-5:]

for a, b in cuts:
    g.remove_edge(a, b)

a, b = [len(x) for x in nx.connected_components(g)]

print_answers(a * b, None, day=25)  # Correct: 614655
