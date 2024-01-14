from utils import read, print_answers


def is_caught(time, range):
    return time % ((range - 1) * 2) == 0


raw = read(2017, 13).split("\n")
fwall = [tuple(map(int, line.split(": "))) for line in raw]

a1 = sum([d * r * is_caught(d, r) for d, r in fwall])
a2 = next(dl for dl in range(5_000_000) if not any(is_caught(d + dl, r) for d, r in fwall))

print_answers(a1, a2, day=13)  # 2688 3876272
