from collections import deque
from utils import read, print_answers


def solve(ref, spins, steps):
    slock = deque([0])

    for i in range(1, spins + 1):
        slock.rotate(-steps)
        slock.append(i)

    return slock[(slock.index(ref) + 1) % len(slock)]


steps = int(read(2017, 17))

a1 = solve(2017, 2017, steps)
a2 = solve(0, 50_000_000, steps)

print_answers(a1, a2, day=17)  # 1311 39170601
