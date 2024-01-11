from utils import read_input
from itertools import combinations
from functools import reduce
from operator import mul


def solve(numbers, combination_length):
    for tryout in combinations(numbers, combination_length):
        if sum(tryout) == 2020:
            return reduce(mul, tryout)
    print("Answer not found")


if __name__ == "__main__":
    entries = [int(x) for x in read_input("inputs/day_01.txt")]

    answer_1 = solve(entries, combination_length=2)
    answer_2 = solve(entries, combination_length=3)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
