import re

from utils import read_input


def process_a(to_process):
    FIRST_REST_SPLITTER = r"([0-9]* [\+*] [0-9]*)(.*)"

    while len(to_process.split()) > 1:
        m = re.match(FIRST_REST_SPLITTER, to_process)
        first_pair, rest = m.group(1), m.group(2)
        to_process = str(eval(first_pair)) + rest
    return int(to_process)


def process_b(to_process):
    ADDITION_OP = r"[0-9]* \+ [0-9]*"

    while "+" in to_process:
        add_op = re.search(ADDITION_OP, to_process)[0]
        to_process = re.sub(ADDITION_OP, str(eval(add_op)), to_process, count=1)
    return int(eval(to_process))


def solve(line, method):
    INNERMOST_PARENS = r"\([0-9 \+*]*\)"

    while True:
        m = re.search(INNERMOST_PARENS, line)
        if m:
            subgroup = m[0]
            processed = method(subgroup[1:-1])
            line = re.sub(INNERMOST_PARENS, str(processed), line, count=1)
        else:
            return method(line)


if __name__ == "__main__":
    raw_in = read_input("inputs/day_18.txt")

    answer_1 = sum(solve(line, method=process_a) for line in raw_in)
    answer_2 = sum(solve(line, method=process_b) for line in raw_in)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
