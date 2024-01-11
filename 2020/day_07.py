import re

from utils import read_input


def parse_type_and_amount(c):
    as_list = c.split()
    amount = int(as_list[0])
    bag_type = " ".join(as_list[1:])
    return (bag_type, amount)


def parse_rule(rule):
    cleaned = rule.replace(".", "").replace("bags", "bag")
    holder, contents_str = cleaned.split(" contain ")

    if contents_str == "no other bag":
        d = {}
    else:
        contents = [b.strip() for b in contents_str.split(",")]
        d = {k: v for k, v in map(parse_type_and_amount, contents)}
    return (holder, d)


def parse_rules(raw_in):
    return dict(parse_rule(r) for r in raw_in)


def create_ancestry_dict(rules):
    d = {b: set() for b in rules}
    for b, children in rules.items():
        for c in children:
            d[c].add(b)
    return d


def get_unique_ancestors(ancestry, bag_name):
    if ancestry[bag_name] == set():
        return set()
    else:
        parents = ancestry[bag_name]
        further_ancestors = set.union(
            *(get_unique_ancestors(ancestry, b) for b in ancestry[bag_name])
        )
        return parents | further_ancestors


def calculate_descendants(rules, bag_name):
    if rules[bag_name] == {}:
        return 0
    else:
        n_children = sum(v for v in rules[bag_name].values())
        n_further_descendants = sum(
            v * calculate_descendants(rules, k) for k, v in rules[bag_name].items()
        )
        return n_children + n_further_descendants


if __name__ == "__main__":
    raw_in = read_input("inputs/day_07.txt")
    rules = parse_rules(raw_in)

    ancestry = create_ancestry_dict(rules)
    unique_ancestors = get_unique_ancestors(ancestry, "shiny gold bag")
    answer_2 = calculate_descendants(rules, "shiny gold bag")

    print(f"Part 1 answer: {len(unique_ancestors)}")
    print(f"Part 2 answer: {answer_2}")
