import re
from utils import read_file, print_answers


def parse_input(raw_in):
    a, b = raw_in.split("\n\n")

    # Parse stacks
    get_letters = lambda l: [l[i] for i in range(1, len(l), 4)]
    get_stack = lambda l: "".join(l)[:-1].strip()
    letters = [get_letters(l) for l in a.split("\n")]
    stacks = [get_stack(l) for l in zip(*letters)]

    # Parse instructions
    get_instrs = lambda s: list(map(int, re.findall("\d+", s)))
    correct_idxs = lambda a, b, c: (a, b - 1, c - 1)
    instructions = [correct_idxs(*get_instrs(x)) for x in b.split("\n")]

    return stacks, instructions


def solve(stacks, instructions, one_only: bool):
    s = stacks.copy()
    for n, fr, to in instructions:
        dir = -1 if one_only else 1
        s[to] = s[fr][:n][::dir] + s[to]
        s[fr] = s[fr][n:]
    return "".join([x[0] for x in s])


if __name__ == "__main__":
    raw_in = read_file("inputs/day_05b.txt")

    stacks, instructions = parse_input(raw_in)

    a1 = solve(stacks, instructions, one_only=True)
    a2 = solve(stacks, instructions, one_only=False)

    print_answers(a1, a2, day=5)
