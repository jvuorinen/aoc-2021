import re
import sys
from utils import read_file, print_answers

sys.setrecursionlimit(5000)


def parse(file):
    raw_in = read_file(file).split()

    start = 1 + 0j
    end = complex(len(raw_in[0]) - 2, len(raw_in) - 1)

    grid = {}
    for i, row in enumerate(raw_in):
        for j, x in enumerate(row):
            grid[complex(j, i)] = x

    nodes = [start]
    for c in grid:
        ns = "".join([grid.get(c + d, ".") for d in [1, -1, 1j, -1j]])
        if len(re.findall(r"[<>^v]", ns)) >= 3:
            nodes.append(c)

    nodes.append(end)
    return grid, nodes, start, end


def find_distances(path, last_node, steps, dist):
    if path[-1] != end:
        for d in [1, -1, 1j, -1j]:
            nxt = path[-1] + d
            if (grid.get(nxt, "#") == "#") or (nxt in path):
                continue
            if grid[nxt] == ">" and d != 1:
                continue
            if grid[nxt] == "<" and d != -1:
                continue
            if grid[nxt] == "^" and d != -1j:
                continue
            if grid[nxt] == "v" and d != 1j:
                continue
            if nxt in nodes:
                dist[last_node][nxt] = steps
                last_node = nxt
                steps = 0
            find_distances(path + [nxt], last_node, steps + 1, dist)


def crawl(n, res, d=0, seen=None):
    if not seen:
        seen = set([n])
    if n == end:
        res.append(d)
        return
    for _n, _d in dist[n].items():
        if _n not in seen:
            crawl(_n, res, d + _d, seen | {_n})


if __name__ == "__main__":
    grid, nodes, start, end = parse("inputs/day_23b.txt")

    dist = {n: {} for n in nodes}
    find_distances([start], start, 1, dist)

    res = []
    crawl(start, res)
    a1 = max(res)

    # Add backward connections
    for a, ns in dist.items():
        for b, x in ns.items():
            dist[b][a] = x

    res = []
    crawl(start, res)
    a2 = max(res)

    print_answers(a1, a2, day=23)  # Correct: 2358, 6586
