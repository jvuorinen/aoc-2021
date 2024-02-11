from utils import read, print_answers

MAGIC_NUMBER = int(read(2016, 13))


def is_wall(loc):
    x, y = loc.real, loc.imag
    if x < 0 or y < 0:
        return True
    num = int(x * x + 3 * x + 2 * x * y + y + y * y + MAGIC_NUMBER)
    return bin(num)[2:].count("1") % 2 == 1


def crawl(loc):
    seen, history = set(), []
    Q = [(loc, 0)]
    while Q:
        x, s = Q.pop(0)
        if x not in seen:
            seen.add(x)
            history.append((x, s))
        for d in (-1, 1, -1j, 1j):
            if not is_wall(_x := x + d) and _x not in seen:
                Q.append((_x, s + 1))
    return history


history = crawl(1 + 1j)
a1 = next(st for loc, st in history if loc == 31 + 39j)
a2 = sum(1 for _, st in history if st <= 50)

print_answers(a1, a2, day=13)
