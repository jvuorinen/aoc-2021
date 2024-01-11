from functools import lru_cache

import numpy as np

from utils import read_input


def get_ordered_joltages(raw_in):
    s = sorted(int(x) for x in raw_in)
    a = tuple([0] + s + [max(s) + 3])
    return a


def solve_1(joltages):
    diffs = np.diff(joltages)
    return sum(diffs == 1) * sum(diffs == 3)


def get_antecedent_idxes(adapter_idx, joltages):
    candidates = [(adapter_idx - i) for i in (1, 2, 3) if (adapter_idx - i) >= 0]
    valid = [c for c in candidates if (joltages[adapter_idx] - joltages[c]) <= 3]
    return valid


@lru_cache(maxsize=None)
def get_n_paths_to(adapter_idx, joltages):
    if adapter_idx == 0:
        return 1
    else:
        antecedent_idxs = get_antecedent_idxes(adapter_idx, joltages)
        return sum(get_n_paths_to(a, joltages) for a in antecedent_idxs)


if __name__ == "__main__":
    raw_in = read_input("inputs/day_10.txt")
    joltages = get_ordered_joltages(raw_in)

    answer_1 = solve_1(joltages)

    max_adapter_idx = len(joltages) - 1
    answer_2 = get_n_paths_to(max_adapter_idx, joltages)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
