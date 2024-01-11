from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_xx.txt")
    return raw_in


def solve_1(inputs):
    return False


def solve_2(inputs):
    return False


if __name__ == "__main__":
    inputs = get_cleaned_input()

    answer_1 = solve_1(inputs)
    answer_2 = solve_2(inputs)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
