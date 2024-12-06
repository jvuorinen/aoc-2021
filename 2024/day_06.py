from utils import read, print_answers


def run(area):
    loc = next(k for k, v in area.items() if v == "^")
    hdg = 1j
    seen = set()
    while loc in area:
        if (state := (loc, hdg)) in seen:
            return "loop"
        seen.add(state)
        while area.get(loc + hdg) == "#":
            hdg *= -1j
        loc += hdg
    return len(set(x[0] for x in seen))


raw = read(2024, 6).split("\n")
area = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}

a1 = run(area)

candidates = [k for k, v in area.items() if v == "."]
a2 = [run(area | {c: "#"}) for c in candidates].count("loop")

print_answers(a1, a2, day=6)
