from utils import read_file, print_answers


def chunks(it, n):
    return [it[i : i + n] for i in range(0, len(it), n)]


def halve(sack):
    h = len(sack) // 2
    return sack[:h], sack[h:]


def get_value(sacks):
    x = set.intersection(*map(set, sacks)).pop()
    return ord(x) - 96 if x.islower() else ord(x) - 38


if __name__ == "__main__":
    sacks = read_file("inputs/day_03.txt").split()

    a1 = sum([get_value(halve(s)) for s in sacks])
    a2 = sum([get_value(c) for c in chunks(sacks, 3)])

    print_answers(a1, a2, day=3)
