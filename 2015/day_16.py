import re
from utils import read, print_answers

checks = {
    "children": lambda x: x == 3,
    "cats": lambda x: x == 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x == 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x == 5,
    "trees": lambda x: x == 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1,
}

part2 = {
    "cats": lambda x: x > 7,
    "pomeranians": lambda x: x < 3,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
}


def solve(checks, data):
    for i, d in enumerate(data):
        if all(checks[k](v) for k, v in d.items()):
            return i + 1


raw = read(2015, 16).split("\n")
data = [{a: int(b) for a, b in re.findall(r"([^: ]+): (\d+)", line)} for line in raw]

a1 = solve(checks, data)
a2 = solve(checks | part2, data)
print_answers(a1, a2, day=16)
