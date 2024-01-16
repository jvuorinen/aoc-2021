from numba import njit
from utils import read, print_answers

M = 2147483647


@njit
def generator(val, mul, skip=1):
    while True:
        val = val * mul % M
        if val % skip == 0:
            yield val


@njit
def do(a, b, sims):
    gen_a = generator(a, 16807, 4)
    gen_b = generator(b, 48271, 8)

    c = 0
    for _ in range(1, sims + 1):
        a = next(gen_a)
        b = next(gen_b)
        if (a - b) % 65536 == 0:
            c += 1
    return c


raw = read(2017, 15).split("\n")
a, b = [int(x.split()[-1]) for x in raw]

a1 = do(a, b, 40_000_000)
a2 = do(a, b, 5_000_000)
print_answers(a1, a2, day=15)  # 2394 285
