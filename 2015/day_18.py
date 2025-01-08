from utils import read, print_answers

CORNERS = (0, 99, 99j, 99 + 99j)


def nbors(z):
    return [z + d for d in (-1 - 1j, -1, -1 + 1j, -1j, 1j, 1 - 1j, 1, 1 + 1j)]


def step(z, A, p2):
    cnt = sum(A.get(x) == "#" for x in nbors(z))
    if p2 and z in CORNERS:
        return "#"
    if A[z] == "#":
        return "#" if cnt in (2, 3) else "."
    return "#" if cnt == 3 else "."


def simulate(A, p2=False):
    for _ in range(100):
        A = {k: step(k, A, p2) for k in A}
    return sum(x == "#" for x in A.values())


raw = read(2015, 18).split("\n")
A = {complex(r, j): x for r, line in enumerate(raw) for j, x in enumerate(line)}

a1 = simulate(A)
a2 = simulate(A | {z: "#" for z in CORNERS}, p2=True)

print_answers(a1, a2, day=18)
