import networkx as nx
from utils import read, print_answers

raw = read(2017, 12).split("\n")

G = nx.Graph()
for line in raw:
    a, bs = line.split(" <-> ")
    for b in bs.split(", "):
        G.add_edge(int(a), int(b))

a1 = len(nx.descendants(G, 0)) + 1
a2 = len([*nx.connected_components(G)])

print_answers(a1, a2, day=12)  # 288
