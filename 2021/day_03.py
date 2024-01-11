import numpy as np

from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_03.txt")
    array = np.array([x for x in map(list, raw_in)]).astype(int)
    return array


def invert(array):
    return (~array.astype(bool)).astype(int)


def to_int(array):
    return int("".join(array.astype(str)), 2)


def solve_1(array):
    gamma = array.mean(axis=0).round().astype(int)

    epsilon = invert(gamma)
    result = to_int(gamma) * to_int(epsilon)
    return result


def reduce_array(array, bit_criteria):
    tmp = array.copy()
    for i in range(array.shape[1]):
        col = tmp[:, i]
        filter = col == bit_criteria(col)
        tmp = tmp[filter, :]
        if len(tmp) == 1:
            return tmp[0]


def solve_2(array):
    most_common_func = lambda col: (col.mean() + 1e-15).round().astype(int)
    least_common_func = lambda col: (invert(col).mean() - 1e-15).round().astype(int)

    oxygen = reduce_array(array, most_common_func)
    co2 = reduce_array(array, least_common_func)

    result = to_int(oxygen) * to_int(co2)
    return result


if __name__ == "__main__":
    array = get_cleaned_input()

    answer_1 = solve_1(array)
    answer_2 = solve_2(array)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
