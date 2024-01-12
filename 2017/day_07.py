from collections import Counter
import re
import networkx as nx
from utils import read, print_answers


def parse_graph(raw):
    G = nx.DiGraph()
    for line in raw:
        n, w, *children = re.findall(r"\w+", line)
        G.add_node(n, weight=int(w))
        for c in children:
            G.add_edge(n, c)
    return G


def total_weight(G, node):
    desc_weight = sum([G.nodes[x]["weight"] for x in nx.descendants(G, node)])
    return G.nodes[node]["weight"] + desc_weight


def get_problem(node):
    children = [x for x in G.successors(node)]
    weights = [total_weight(G, x) for x in children]
    counts = Counter(weights)
    if len(counts) > 1:
        bad_weight, good_weight = sorted(counts, key=counts.get)
        return children[weights.index(bad_weight)], good_weight


raw = read(2017, 7).split("\n")

G = parse_graph(raw)
root = next(nx.topological_sort(G))

node = root
while problem := get_problem(node):
    node, good_weight = problem

adjustment = total_weight(G, node) - good_weight
a2 = G.nodes[node]["weight"] - adjustment

print_answers(root, a2, day=7)  # azqje 646
