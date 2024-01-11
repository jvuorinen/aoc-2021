from itertools import combinations
from utils import read_file, print_answers
import numpy as np
import sympy as sym


def parse(file):
    hails = []
    for line in read_file(file).split("\n"):
        h = line.split(" @ ")
        hails.append([tuple([*map(int, x.split(","))]) for x in h])
    return hails


def do_cross(h1, h2, dmin, dmax):
    (ax, ay, _), (adx, ady, _) = h1
    (bx, by, _), (bdx, bdy, _) = h2

    A = [[adx, -bdx], [ady, -bdy]]
    b = [bx - ax, by - ay]

    if np.linalg.det(A) == 0:
        return False

    sol = np.linalg.solve(A, b)
    if len(sol) == 0 or any(x < 0 for x in sol):
        return False

    x = ax + sol[0] * adx
    y = ay + sol[0] * ady
    return all((dmin <= d <= dmax) for d in (x, y))


def get_perfect_throw(hails):
    hails = hails[:3]  # Any 3 hails is enough to determine the throw
    x, y, z, dx, dy, dz, t1, t2, t3 = sym.symbols("x,y,z,dx,dy,dz,t1,t2,t3")

    eqs = []
    for t, hail in zip((t1, t2, t3), hails):
        (_x, _y, _z), (_dx, _dy, _dz) = hail

        eqs.extend(
            [
                sym.Eq(x + t * dx, _x + t * _dx),
                sym.Eq(y + t * dy, _y + t * _dy),
                sym.Eq(z + t * dz, _z + t * _dz),
            ]
        )
    return sym.solve(eqs, (x, y, z, dx, dy, dz, t1, t2, t3))[0]


hails = parse("inputs/day_24b.txt")

a1 = sum([do_cross(h1, h2, 2e14, 4e14) for h1, h2 in combinations(hails, 2)])
a2 = sum(get_perfect_throw(hails)[:3])

print_answers(a1, a2, day=None)  # Correct: 14046, 808107741406756
