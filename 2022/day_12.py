from utils import read_file, print_answers, get_neighbors, get_bounds
import numpy as np
from string import ascii_lowercase
from collections import defaultdict


def parse(raw_in):
    chars = np.array([list(r) for r in raw_in])
    start = tuple([x[0] for x in np.where(chars == "S")])
    end = tuple([x[0] for x in np.where(chars == "E")])

    chars[chars == "S"] = "a"
    chars[chars == "E"] = "z"
    hmap = np.vectorize(ascii_lowercase.index)(chars)
    candidates = set([c for c in zip(*np.where(hmap == 0))])
    return hmap, start, end, candidates


def bfs(hmap, start, ends):
    queue = [start]
    visited = set([start])
    dist = defaultdict(int)
    bounds = get_bounds(hmap)

    while queue:
        c = queue.pop(0)
        for n in get_neighbors(c, bounds):
            if (n not in visited) and (hmap[n] - hmap[c] <= 1):
                dist[n] = dist[c] + 1
                if n in ends:
                    return dist[n]
                queue.append(n)
                visited.add(n)


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_12b.txt").split()
    hmap, start, end, candidates = parse(raw_in)

    a1 = bfs(hmap, start, set([end]))
    a2 = bfs(-hmap, end, candidates)

    print_answers(a1, a2, day=12)
