from utils import read_file, print_answers
import numpy as np


def parse_xs(program):
    parse = lambda cmd: (1, 0) if cmd[0] == "n" else (2, int(cmd.split()[1]))
    cycles, adds = zip(*[parse(cmd) for cmd in program])
    idxs, adds = zip(*[(i, a) for i, a in zip(np.cumsum(cycles), adds) if a != 0])

    arr = np.zeros(sum(cycles), dtype=int)
    arr[list(idxs)] = adds
    return arr.cumsum() + 1


if __name__ == "__main__":
    program = read_file("inputs/day_10b.txt").split("\n")
    xs = parse_xs(program)

    # Part 1
    a1 = sum([xs[i - 1] * i for i in range(20, len(xs), 40)])

    # Part 2
    ROWS, COLS = 6, 40
    pos = np.tile(np.arange(COLS), ROWS)
    drawn = (abs(xs - pos) < 2).astype(int).reshape(ROWS, COLS)
    chars = np.array([" ", "#"])[drawn]
    a2 = "\n".join(map("".join, chars))

    print_answers(a1, a2, day=10)
