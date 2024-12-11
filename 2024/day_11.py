from functools import cache
from utils import read, print_answers

raw = read(2024, 11)
stones = [*map(int, raw.split())]

@cache
def solve(stone, reps):
    if reps == 0:
        return 1
    nxt = []
    if stone == 0:
        nxt.append(1)
    elif len(ss := str(stone)) % 2 == 0:
        nxt.append(int(ss[:len(ss) // 2]))
        nxt.append(int(ss[len(ss) // 2:]))
    else:
        nxt.append(stone * 2024)
    return sum(solve(n, reps - 1) for n in nxt)

a1 = sum([solve(x, 25) for x in stones])
a2 = sum([solve(x, 75) for x in stones])

print_answers(a1, a2, day=11)
