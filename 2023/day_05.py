from functools import partial, reduce
from utils import print_answers, read_file


def parse_data(raw_in):
    s, *maps = raw_in.split("\n\n")
    seeds = [int(x) for x in s.split(": ")[1].split()]
    network = []
    for m in maps:
        network.append([tuple(map(int, x.split())) for x in m.split("\n")[1:]])
    return seeds, network


def _transform(n, layer, forward=True):
    for y, x, r in layer:
        if not forward:
            x, y = y, x
        if 0 <= (d := n - x) < r:
            return y + d
    return n


def propagate(n, network, forward=True):
    f = _transform if forward else partial(_transform, forward=False)
    nw = network if forward else network[::-1]
    return reduce(f, nw, n)


def get_eval_points(seeds, network):
    seed_bounds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    points = set()
    for i in range(1, len(network)):
        nw, last = network[:i], network[i]
        lows = [x[1] for x in last]
        candidates = [propagate(p, nw, forward=False) for p in lows]
        valid = set([c for c in candidates for lo, hi in seed_bounds if (lo <= c <= hi)])
        points |= valid
    return points


if __name__ == "__main__":
    raw_in = read_file("inputs/day_05b.txt")
    seeds, network = parse_data(raw_in)

    a1 = min([propagate(x, network) for x in seeds])
    a2 = min([propagate(x, network) for x in get_eval_points(seeds, network)])

    print_answers(a1, a2, day=5)  # Correct: 318728750, 37384986
