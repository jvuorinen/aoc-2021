import numpy as np
from dataclasses import dataclass
from utils import read, print_answers, complex_to_tuple

N, S, W, E, L, R = -1j, 1j, -1, 1, -1j, 1j


@dataclass
class Cart:
    pos: complex
    hdg: complex
    turn_ix: int = 0
    crashed: bool = False


arr = np.array([list(line) for line in read("inputs/day_13b.txt").split("\n")])
symbol_locs = zip(*np.where(np.isin(arr, list("^>v<"))))
carts = [Cart(complex(x, y), [N, E, S, W]["^>v<".index(arr[y, x])]) for y, x in symbol_locs]
crashes = []

while len(not_crashed := [c for c in carts if not c.crashed]) > 1:
    carts.sort(key=lambda c: c.pos.real + 100 * c.pos.imag)

    for c in not_crashed:
        c.pos += c.hdg
        others = [o for o in not_crashed if (c != o)]
        for o in others:
            if c.pos == o.pos:
                c.crashed = o.crashed = True
                crashes.append(c.pos)

        match arr[int(c.pos.imag), int(c.pos.real)]:
            case "+":
                c.hdg *= [L, 1, R][c.turn_ix]
                c.turn_ix = (c.turn_ix + 1) % 3
            case "/":
                c.hdg *= (L, R)[c.hdg in (N, S)]
            case "\\":
                c.hdg *= (R, L)[c.hdg in (N, S)]

a1 = ",".join(map(str, complex_to_tuple(crashes[0])))
a2 = ",".join(map(str, complex_to_tuple(not_crashed[0].pos)))
print_answers(a1, a2, day=13)
