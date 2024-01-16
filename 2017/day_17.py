from numba import njit
from utils import read, print_answers


@njit
def solve(ref, spins, steps):
    nxt = [*range(spins + 1)]
    curr = 0
    for i in range(1, spins + 1):
        for _ in range(steps):
            curr = nxt[curr]
        nxt[i] = nxt[curr]
        nxt[curr] = i
        curr = i
    return nxt[ref]


steps = int(read(2017, 17))

a1 = solve(2017, 2017, steps)
a2 = solve(0, 50_000_000, steps)

print_answers(a1, a2, day=17)  # 1311 39170601
