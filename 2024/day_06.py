from utils import read, print_answers


def run(area, start):
    loc, hdg = start, 1j
    seen = set()
    while loc in area:
        if (state := (loc, hdg)) in seen:
            return "loop"
        seen.add(state)
        while area.get(loc + hdg) == "#":
            hdg *= -1j
        loc += hdg
    return set(x[0] for x in seen)


raw = read(2024, 6).split("\n")
area = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}
start = next(k for k, v in area.items() if v == "^")

seen = run(area, start)

a1 = len(seen)
a2 = [run(area | {c: "#"}, start) for c in (seen - {start})].count("loop")

print_answers(a1, a2, day=6)
