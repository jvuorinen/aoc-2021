import re
from utils import read, print_answers


def calculate(program):
    nums = re.findall(r"mul\((\d+),(\d+)\)", program)
    return sum(int(a) * int(b) for a, b in nums)


def flipflop(s, state=True):
    if (delim := "don't" if state else "do()") in s:
        first, rest = s.split(delim, 1)
        return flipflop(first, state) + flipflop(rest, not state)
    return int(state) * calculate(s)


program = read(2024, 3)

a1 = calculate(program)
a2 = flipflop(program)

print_answers(a1, a2, day=3)
