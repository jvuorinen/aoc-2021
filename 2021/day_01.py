from utils import read_input
import numpy as np


def get_cleaned_input():
    raw_in = read_input("inputs/day_01.txt")
    array = np.array(raw_in).astype(int)
    return array


def count_increases(array):
    result = (np.diff(array) > 0).sum()
    return result


if __name__ == "__main__":
    inputs = get_cleaned_input()

    answer_1 = count_increases(inputs)
    answer_2 = count_increases(inputs[:-2] + inputs[1:-1] + inputs[2:])

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
