from numba import njit
from utils import read, print_answers

M = 2147483647


@njit
def generator(val, mul, skip):
    while True:
        val = val * mul % M
        if val % skip == 0:
            yield val


@njit
def do(a, b, sims, skip_a, skip_b):
    gen_a = generator(a, 16807, skip_a)
    gen_b = generator(b, 48271, skip_b)

    c = 0
    for _ in range(1, sims + 1):
        a = next(gen_a)
        b = next(gen_b)
        if (a - b) % 65536 == 0:
            c += 1
    return c


raw = read(2017, 15).split("\n")
a, b = [int(x.split()[-1]) for x in raw]

a1 = do(a, b, 40_000_000, 1, 1)
a2 = do(a, b, 5_000_000, 4, 8)

print_answers(a1, a2, day=15)  # 612 285
