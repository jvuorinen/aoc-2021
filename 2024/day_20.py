from utils import read, print_answers


def get_distances(area):
    floor = set([k for k, v in area.items() if v != "#"])

    todo = [(0, start)]
    steppable = floor.copy()
    P = {}
    while todo:
        i, n = todo.pop(0)
        P[n] = i
        steppable -= {n}
        todo += [(i + 1, nn) for d in (1, -1, 1j, -1j) if (nn := n + d) in steppable]

    L1 = {
        (f, ff): abs(r) + abs(i)
        for r in range(-20, 20 + 1)
        for i in range(-(20 - abs(r)), 20 - abs(r) + 1)
        for f in floor
        if (ff := f + r + 1j * i) in floor
    }
    return P, L1


def length_with_cheat(c1, c2):
    cheat = abs((c1 - c2).real) + abs((c1 - c2).imag)
    return P[c1] + cheat + P[end] - P[c2]


def solve(time, thrs):
    cheats = [c for c, d in L1.items() if 1 < d <= time]
    distances = [d for c in cheats if (d := length_with_cheat(*c))]
    return len([d for d in distances if P[end] - d >= thrs])


raw = read(2024, 20)
area = {c + 1j * r: x for r, line in enumerate(raw.split("\n")) for c, x in enumerate(line)}
start = next(k for k, v in area.items() if v == "S")
end = next(k for k, v in area.items() if v == "E")

P, L1 = get_distances(area)

a1 = solve(time=2, thrs=100)
a2 = solve(time=20, thrs=100)
print_answers(a1, a2, day=20)
