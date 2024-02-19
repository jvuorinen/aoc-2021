from utils import read, print_answers


def resolve(triple):
    return "^" if triple in ("^^.", ".^^", "^..", "..^") else "."


def solve(row, size):
    res = []
    for _ in range(size):
        res.append(row)
        row = "." + row + "."
        row = "".join([resolve("".join(triple)) for triple in zip(row, row[1:], row[2:])])
    return "".join(res).count(".")


row = read(2016, 18)

a1 = solve(row, 40)
a2 = solve(row, 400000)

print_answers(a1, a2, day=18)
