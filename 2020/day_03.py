from utils import read_input, str_to_array
from functools import reduce
from operator import mul


def get_cleaned_input():
    raw = read_input("inputs/day_03.txt")
    arr = str_to_array(raw)

    tree_ascii = 35
    as_boolean = arr == tree_ascii
    return as_boolean


def is_tree(trees, loc_y, loc_x):
    max_y, max_x = trees.shape
    mod_y = loc_y % max_y
    mod_x = loc_x % max_x

    return trees[mod_y, mod_x]


def count_trees(trees, step_y, step_x):
    y, x = 0, 0
    max_y = trees.shape[0] - 1

    results = []
    while y <= max_y:
        res = is_tree(trees, y, x)
        results.append(res)
        y += step_y
        x += step_x

    n_trees = sum(results)
    return n_trees


def solve_2(trees):
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    results = [count_trees(trees, step_y, step_x) for step_y, step_x in slopes]
    return reduce(mul, results)


if __name__ == "__main__":
    trees = get_cleaned_input()

    answer_1 = count_trees(trees, step_y=1, step_x=3)
    answer_2 = solve_2(trees)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
