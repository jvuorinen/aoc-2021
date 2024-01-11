from utils import read_file, print_answers
import re

NUMERALS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_value(num):
    digits = [x for x in num if x.isdigit()]
    return int(digits[0] + digits[-1])


def digify(num):
    for i, n in enumerate(NUMERALS, 1):
        num = re.sub(str(i), n, num)

    p = re.compile(f'(?=({"|".join(NUMERALS)}))')
    matches = re.findall(p, num)
    return "".join([str(NUMERALS.index(x) + 1) for x in matches])


if __name__ == "__main__":
    raw_in = read_file("inputs/day_01.txt").split("\n")

    a = sum([get_value(x) for x in raw_in])
    b = sum([get_value(digify(x)) for x in raw_in])

    print_answers(a, b, day=1)  # Correct: 54304, 54418
