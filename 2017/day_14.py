from functools import reduce
from itertools import chain
import networkx as nx
from utils import read, print_answers


def knot(word, times=64):
    lst = [x for x in range(256)]
    inputs = [*map(ord, word)] + [17, 31, 73, 47, 23]
    s = 0
    for sk, ip in enumerate(inputs * times):
        lst = lst[:ip][::-1] + lst[ip:]
        p = (ip + sk) % len(lst)
        s += p
        lst = lst[p:] + lst[:p]
    st = -s % len(lst)
    lst = lst[st:] + lst[:st]
    dense = [reduce(int.__xor__, lst[i : i + 16]) for i in range(0, len(lst), 16)]
    hx = chain(*((x // 16, x % 16) for x in dense))
    bn = "".join(f"{x:04b}" for x in hx)
    return bn


word = read(2017, 14)
ones = set([i + j * 1j for j in range(128) for i, c in enumerate(knot(f"{word}-{j}")) if c == "1"])

G = nx.Graph()
for x in ones:
    G.add_edge(x, x)
    for d in (1, 1j):
        if (n := x + d) in ones:
            G.add_edge(x, n)

a1 = len(ones)
a2 = nx.number_connected_components(G)

print_answers(a1, a2, day=14)  # 8250 1113
