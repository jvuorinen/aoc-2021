from math import lcm
from itertools import cycle
from utils import read_file, print_answers


def parse(raw_in):
    cmds, doors = raw_in.split("\n\n")
    doors = [x.split(" = ") for x in doors.split("\n")]
    doors = {a: tuple(b[1:-1].split(", ")) for a, b in doors}
    return cmds, doors


def travel(cmds, doors, start):
    visited = set([(0, start)])
    path = [start]

    for i in cycle(range(len(cmds))):
        nxt = doors[path[-1]][cmds[i] == "R"]
        path.append(nxt)
        token = (i, nxt)
        if token in visited:
            return path
        visited.add(token)


if __name__ == "__main__":
    raw_in = read_file("inputs/day_08b.txt")
    cmds, doors = parse(raw_in)

    a1 = travel(cmds, doors, "AAA").index("ZZZ")

    starts = [d for d in doors if d[-1] == "A"]
    routes = [travel(cmds, doors, s) for s in starts]
    ends = [next(i for i, x in enumerate(r) if x[-1] == "Z") for r in routes]
    a2 = lcm(*ends)

    print_answers(a1, a2, day=8)  # Correct: 13939, 8906539031197
