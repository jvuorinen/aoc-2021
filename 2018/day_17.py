import re
from utils import read, print_answers


def parse(file):
    pat = r"(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)"
    clay = set()
    for line in read(file).split("\n"):
        a, b, _, d, e = re.findall(pat, line)[0]
        b, d, e = map(int, [b, d, e])
        for x in range(d, e + 1):
            clay.add((b + x * 1j) if a == "x" else (x + b * 1j))
    return clay


def find_bounds(d, clay, frozen):
    interval = set()
    closed = [True, True]
    for idx, hdg in enumerate([-1, 1]):
        for i in range(1000):
            x = d + hdg * i
            if x in clay:
                break
            interval.add(x)
            below = x + 1j
            if (below not in clay) and (below not in frozen):
                closed[idx] = False
                break
    return interval, closed


def simulate(clay):
    depths = [c.imag for c in clay]
    MIN_DEPTH = min(depths)
    MAX_DEPTH = max(depths)

    touched = set()
    frozen = set()
    drops = [500 + MIN_DEPTH * 1j]

    while drops:
        d = drops.pop()

        while (d + 1j not in clay) and (d.imag <= MAX_DEPTH):
            touched.add(d)
            d += 1j

        if (d.imag < MAX_DEPTH) and (d not in touched):
            touched.add(d)

            while True:
                interval, closed = find_bounds(d, clay, frozen)
                if not all(closed):
                    break
                frozen |= interval
                d -= 1j

            _iv = sorted(interval, key=lambda x: x.real)
            bounds = _iv[0], _iv[-1]
            for i, b in enumerate(bounds):
                if not closed[i]:
                    drops.append(b)
            touched |= interval
    return touched, frozen


clay = parse("inputs/day_17b.txt")
touched, frozen = simulate(clay)

a1 = len(touched | frozen)
a2 = len(frozen)
print_answers(a1, a2, day=17)  # 41027, 34214
