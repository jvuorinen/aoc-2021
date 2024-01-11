from utils import read_file, print_answers
import re


def parse(r):
    return [int(x) for x in re.findall("\d+", r)]


def check_contains(a0, a1, b0, b1):
    return (a0 <= b0 <= b1 <= a1) or (b0 <= a0 <= a1 <= b1)


def check_overlaps(a0, a1, b0, b1):
    return not ((a0 > b1) or (b0 > a1))


if __name__ == "__main__":
    raw_in = read_file("inputs/day_04b.txt").split()

    a1 = sum([check_contains(*parse(r)) for r in raw_in])
    a2 = sum([check_overlaps(*parse(r)) for r in raw_in])

    print_answers(a1, a2, day=4)
