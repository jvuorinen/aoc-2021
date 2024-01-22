from utils import read, print_answers

DIRS = {"U": -1j, "D": 1j, "L": -1, "R": 1}


def solve(cmds, keypad):
    res = []
    loc = 1 + 1j
    for cmd in cmds:
        for c in cmd:
            loc = _loc if (_loc := loc + DIRS[c]) in keypad else loc
        res.append(keypad[loc])
    return "".join(res)


cmds = read(2016, 2).split("\n")

keypad1 = {
    0: "1",
    1: "2",
    2: "3",
    1j: "4",
    1 + 1j: "5",
    2 + 1j: "6",
    2j: "7",
    1 + 2j: "8",
    2 + 2j: "9",
}

keypad2 = {
    2: "1",
    1 + 1j: "2",
    2 + 1j: "3",
    3 + 1j: "4",
    0 + 2j: "5",
    1 + 2j: "6",
    2 + 2j: "7",
    3 + 2j: "8",
    4 + 2j: "9",
    1 + 3j: "A",
    2 + 3j: "B",
    3 + 3j: "C",
    2 + 4j: "D",
}

a1 = solve(cmds, keypad1)
a2 = solve(cmds, keypad2)
print_answers(a1, a2, day=99)  # 47978 659AD
