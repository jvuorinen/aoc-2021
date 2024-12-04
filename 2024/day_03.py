import re
from utils import read, print_answers


def calculate(prg):
    nums = re.findall(r"mul\((\d+),(\d+)\)", prg)
    return sum(int(a) * int(b) for a, b in nums)


def flipflop(prg, state=True):
    if (delim := "don't" if state else "do()") in prg:
        first, rest = prg.split(delim, 1)
        return flipflop(first, state) + flipflop(rest, not state)
    return int(state) * calculate(prg)


program = read(2024, 3)

a1 = calculate(program)
a2 = flipflop(program)

print_answers(a1, a2, day=3)
