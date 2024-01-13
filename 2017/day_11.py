from utils import read, print_answers


DIRS = {
    "n": -2j,
    "s": 2j,
    "nw": -1 - 1j,
    "ne": 1 - 1j,
    "sw": -1 + 1j,
    "se": 1 + 1j,
}


def dist(loc):
    r, i = abs(loc.real), abs(loc.imag)
    return int(r + max(0, i - r) / 2)


dirs = read(2017, 11).split(",")

loc = 0j
hist = [loc := loc + DIRS[d] for d in dirs]
ds = [dist(x) for x in hist]

a1 = ds[-1]
a2 = max(ds)

print_answers(a1, a2, day=11)  # 824 1548
