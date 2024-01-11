import networkx as nx

from utils import read_input


def parse_inputs(raw_in):
    foods = []
    for line in raw_in:
        i, a = line[:-1].split(" (contains ")
        ingredients = set(i.split())
        allergens = set(a.split(", "))
        foods.append((ingredients, allergens))
    return foods


def max_flow_solve(foods):
    G = nx.DiGraph()

    tmp_m, tmp_n = zip(*foods)
    all_i = set.union(*tmp_m)
    all_a = set.union(*tmp_n)
    allg_holders = {allg: set(i for i, f in enumerate(foods) if allg in f[1]) for allg in all_a}

    for i in all_i:
        G.add_edge("source", i, capacity=1.0)
        G.add_edge(i, "safe")
    for a in all_a:
        G.add_edge(a, "sink", capacity=1.0)
        possible_i = set.intersection(*(foods[f][0] for f in allg_holders[a]))
        for i in possible_i:
            G.add_edge(i, a, capacity=1.0)

    G.add_edge("safe", "sink", capacity=len(all_i) - len(all_a))

    _, flow_dict = nx.maximum_flow(G, "source", "sink")
    solution = {k: max(v, key=v.get) for k, v in flow_dict.items() if k in all_i}
    return solution


if __name__ == "__main__":
    raw_in = read_input("inputs/day_21.txt")
    foods = parse_inputs(raw_in)

    allg_map = max_flow_solve(foods)

    safe_ingts = {k for k, v in allg_map.items() if v == "safe"}
    allergens = {k: v for k, v in allg_map.items() if v != "safe"}

    answer_1 = sum(1 for igt in safe_ingts for f in foods if igt in f[0])
    answer_2 = ",".join(sorted(allergens, key=allg_map.get))

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
