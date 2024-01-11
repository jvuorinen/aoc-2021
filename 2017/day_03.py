from utils import read, print_answers


def stepgen():
    hdg = 1
    for n in range(1, 1000):
        for _ in range(2):
            for _ in range(n):
                yield hdg
            hdg *= 1j


def solve_1(num):
    sg = stepgen()
    x = sum([next(sg) for _ in range(num - 1)])
    return int(abs(x.real) + abs(x.imag))


def solve_2(num):
    mem = {0: 1}
    c = 0
    sg = stepgen()
    while mem[c] <= num:
        c += next(sg)
        offsets = [n for i in (-1, 0, 1) for j in (-1j, 0, 1j) if (n := i + j) != 0]
        mem[c] = sum([mem.get(c + d, 0) for d in offsets])
    return mem[c]


num = int(read(2017, 3))

a1 = solve_1(num)
a2 = solve_2(num)

print_answers(a1, a2, day=3)  # 430 312453
