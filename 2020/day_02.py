import numpy as np

from utils import read_input


def parse_line(line):
    policy, pw = line.split(": ")
    nums_raw, letter = policy.split(" ")
    num_low, num_high = [int(i) for i in nums_raw.split("-")]
    return num_low, num_high, letter, pw


def validate_simple(line):
    num_low, num_high, letter, pw = parse_line(line)

    is_valid = num_low <= pw.count(letter) <= num_high
    return is_valid


def validate_complex(line):
    num_low, num_high, letter, pw = parse_line(line)

    first_equals = pw[num_low - 1] == letter
    second_equals = pw[num_high - 1] == letter

    is_valid = sum([first_equals, second_equals]) == 1
    return is_valid


def sum_of_valids(password_list, func):
    return sum(func(x) for x in password_list)


if __name__ == "__main__":
    password_list = read_input("inputs/day_02.txt")

    answer_1 = sum_of_valids(password_list, validate_simple)
    answer_2 = sum_of_valids(password_list, validate_complex)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
