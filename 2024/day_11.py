from functools import cache
from utils import read, print_answers

raw = read(2024, 11)
stones = [*map(int, raw.split())]


@cache
def solve(stone, reps):
    if reps == 0:
        return 1
    if stone == 0:
        return solve(1, reps - 1)
    elif len(ss := str(stone)) % 2 == 0:
        a = int(ss[: len(ss) // 2])
        b = int(ss[len(ss) // 2 :])
        return solve(a, reps - 1) + solve(b, reps - 1)
    return solve(2024 * stone, reps - 1)


a1 = sum([solve(x, 25) for x in stones])
a2 = sum([solve(x, 75) for x in stones])

print_answers(a1, a2, day=11)
