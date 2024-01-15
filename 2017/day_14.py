import networkx as nx
from day_10 import knot
from utils import read, print_answers


def binknot(word):
    return f"{int(knot(word), 16):0128b}"


word = read(2017, 14)
ones = set(
    [i + j * 1j for j in range(128) for i, c in enumerate(binknot(f"{word}-{j}")) if c == "1"]
)

G = nx.Graph()
for x in ones:
    G.add_edge(x, x)
    for d in (1, 1j):
        if (n := x + d) in ones:
            G.add_edge(x, n)

a1 = len(ones)
a2 = nx.number_connected_components(G)

print_answers(a1, a2, day=14)  # 8250 1113
