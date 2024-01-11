import numpy as np
from utils import print_answers, read_file


def parse(raw_in):
    grid = {}
    for i, row in enumerate(raw_in):
        for j, x in enumerate(row):
            if x == "S":
                grid[complex(j, i)] = "."
                start = complex(j, i)
            else:
                grid[complex(j, i)] = x
    return grid, start


def get_cumulative(grid, start, limit):
    size = int(np.sqrt(len(grid)))
    Q = [(start, limit)]
    visited = set()
    collection = [set() for _ in range(limit + 1)]

    while Q:
        x, n = Q.pop(0)
        visited.add(x)
        collection[limit - n].add(x)
        for d in [1, -1, 1j, -1j]:
            nxt = x + d
            modded = complex(nxt.real % size, nxt.imag % size)
            if (nxt not in visited) and (n > 0) and grid.get(modded, "#") == ".":
                Q.append((nxt, n - 1))
                visited.add(nxt)

    counts = [len(x) for x in collection]
    cum = [0] * len(counts)
    cum[::2] = np.cumsum(counts[::2])
    cum[1::2] = np.cumsum(counts[1::2])
    return cum


def get_count(cum, steps):
    if steps < len(cum):
        return cum[steps]

    period = int(np.sqrt(len(grid)))
    lagged = [y - x for x, y in zip(cum[:-period], cum[period:])]
    diffs = list(np.diff(lagged))

    # Identify cycle within diffs
    for i in range(len(diffs)):
        if (cycle := diffs[i : i + period]) == diffs[i + period : i + 2 * period]:
            begin = i
            break

    div, mod = divmod(steps - begin, period)
    ref_idx = begin + mod
    to_add = int(div * lagged[ref_idx] + div * (div - 1) * 0.5 * sum(cycle))
    return cum[ref_idx] + to_add


raw_in = read_file("inputs/day_21b.txt").split()
grid, start = parse(raw_in)

cum = get_cumulative(grid, start, 500)

a1 = get_count(cum, 64)
a2 = get_count(cum, 26501365)

print_answers(a1, a2, day=21)  # Correct: 3682, 609012263058042
