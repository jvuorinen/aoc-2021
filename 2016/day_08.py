import numpy as np
from utils import read, print_answers


def draw(screen):
    d = np.full_like(screen, dtype=str, fill_value=" ")
    d[screen] = "#"
    return "\n".join(map("".join, d))


cmds = read(2016, 8).split("\n")

screen = np.zeros((6, 50), bool)
for cmd in cmds:
    words = cmd.split(" ")
    if words[0] == "rect":
        c, r = map(int, words[1].split("x"))
        screen[:r, :c] = True
    else:
        x = int(words[2].split("=")[1])
        n = int(words[4])
        if words[1] == "column":
            screen[:, x] = np.roll(screen[:, x], n)
        else:
            screen[x, :] = np.roll(screen[x, :], n)

a1 = screen.sum()
a2 = draw(screen)

print_answers(a1, a2, day=8)
