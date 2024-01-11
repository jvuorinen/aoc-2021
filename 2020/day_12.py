from utils import read_input

DIRS = {"N": 1j, "E": 1, "S": -1j, "W": -1}
ROTS = {"R": -1, "L": 1}


def solve(actions, wpt, pos_moves_instead_of_wpt):
    pos = complex(0, 0)
    for a in actions:
        cmd, value = a[0], int(a[1:])
        if cmd in "NSEW":
            if pos_moves_instead_of_wpt:
                pos += value * DIRS[cmd]
            else:
                wpt += value * DIRS[cmd]
        elif cmd in "LR":
            wpt = (1j ** (ROTS[cmd] * (value / 90))) * wpt
        elif cmd == "F":
            pos += value * wpt
    return int(abs(pos.real) + abs(pos.imag))


if __name__ == "__main__":
    actions = read_input("inputs/day_12.txt")

    answer_1 = solve(actions, wpt=complex(1, 0), pos_moves_instead_of_wpt=True)
    answer_2 = solve(actions, wpt=complex(10, 1), pos_moves_instead_of_wpt=False)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
