from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_02.txt")
    commands = [(a, int(b)) for a, b in map(str.split, raw_in)]
    return commands


def solve_1(commands):
    hor = depth = 0

    for cmd, amount in commands:
        if cmd == "forward":
            hor += amount
        elif cmd == "down":
            depth += amount
        elif cmd == "up":
            depth -= amount

    return hor * depth


def solve_2(commands):
    hor = depth = aim = 0

    for cmd, amount in commands:
        if cmd == "forward":
            hor += amount
            depth += aim * amount
        elif cmd == "down":
            aim += amount
        elif cmd == "up":
            aim -= amount

    return hor * depth


if __name__ == "__main__":
    commands = get_cleaned_input()

    answer_1 = solve_1(commands)
    answer_2 = solve_2(commands)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
