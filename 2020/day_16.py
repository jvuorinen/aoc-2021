from copy import deepcopy
from functools import reduce
from operator import mul

import numpy as np
import networkx as nx

from utils import read_input


def _range_to_set(rng):
    l, h = map(int, rng.split("-"))
    return set(i for i in range(l, h + 1))


def _parse_validity(line):
    a, b = line.split(": ")
    valids = reduce(set.union, (_range_to_set(x) for x in b.split(" or ")))
    return (a, valids)


def parse_input(raw_in):
    r, m, o = [x.split("\n") for x in raw_in]

    rules = dict(_parse_validity(x) for x in r)

    to_set = lambda l: tuple(int(x) for x in l.split(","))
    mine = to_set(m[1])
    others = [to_set(x) for x in o[1:]]

    return rules, mine, others


def get_valid_tickets(rules, tickets):
    invalids = set()
    error_rate = 0

    for ticket in tickets:
        for n in ticket:
            if all([(n not in vs) for vs in rules.values()]):
                error_rate += n
                invalids.add(ticket)

    valids = set(tickets) - invalids
    return valids, invalids, error_rate


def build_possibilities_dict(rules, valids):
    possibilities = {}
    tickets = np.array(list(valids))

    for r, vrange in rules.items():
        res = set()
        for i, _ in enumerate(rules):
            if all(v in vrange for v in tickets[:, i]):
                res.add(i)
        possibilities[r] = res
    return possibilities


def max_flow_solve(possibilities):
    G = nx.DiGraph()

    all_m = set(possibilities.keys())
    all_n = set.union(*(s for s in possibilities.values()))

    for m in all_m:
        G.add_edge("source", m, capacity=1.0)
    for n in all_n:
        G.add_edge(n, "sink", capacity=1.0)
    for m, n_ in possibilities.items():
        for n in n_:
            G.add_edge(m, n, capacity=1.0)

    _, flow_dict = nx.maximum_flow(G, "source", "sink")
    return {k: max(v, key=v.get) for k, v in flow_dict.items() if k in all_m}


def solve_2(rules, mine, valids):
    possibilities = build_possibilities_dict(rules, valids)
    solution = max_flow_solve(possibilities)
    idxes = [v for k, v in solution.items() if k.startswith("departure")]
    return reduce(mul, [mine[i] for i in idxes])


if __name__ == "__main__":
    raw_in = read_input("inputs/day_16.txt", split_delimiter="\n\n")
    rules, mine, others = parse_input(raw_in)

    valids, invalids, error_rate = get_valid_tickets(rules, others)
    answer_2 = solve_2(rules, mine, valids)

    print(f"Part 1 answer: {error_rate}")
    print(f"Part 2 answer: {answer_2}")
