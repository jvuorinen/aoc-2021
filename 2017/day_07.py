from collections import Counter
import re
import networkx as nx
from utils import read, print_answers


def parse():
    G = nx.DiGraph()
    for line in read(2017, 7).split("\n"):
        n, w = re.findall(r"([^ ]+) \((.+)\)", line)[0]
        G.add_node(n, weight=int(w))
        if children := re.findall(r"-> (.*)", line):
            for c in children[0].split(", "):
                G.add_edge(n, c)
    return G


def get_weight(G, node):
    desc_weight = sum([G.nodes[x]["weight"] for x in nx.descendants(G, node)])
    return G.nodes[node]["weight"] + desc_weight


def get_problem(node):
    children = [x for x in G.successors(node)]
    weights = [get_weight(G, x) for x in children]
    counts = Counter(weights)
    if len(counts) > 1:
        bad_weight, good_weight = sorted(counts, key=counts.get)
        return children[weights.index(bad_weight)], good_weight

G = parse()
root = next(nx.topological_sort(G))

node = root
while problem := get_problem(node):
    node, good_weight = problem

adjustment = get_weight(G, node) - good_weight
a2 = G.nodes[node]["weight"] - adjustment

print_answers(root, a2, day=7)  # azqje 646
