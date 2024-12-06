from utils import read, print_answers

raw = read()
# raw = read(2024, 6)

area = {c - 1j * r: x for r, line in enumerate(raw.split("\n")) for c, x in enumerate(line)}


# p1
def solve(area, additional_obs=None):
    area = area.copy()
    if additional_obs:
        area[additional_obs] = "#"
    loc = [k for k, v in area.items() if v == "^"][0]
    hdg = 1j

    seen = set()
    while loc in area:
        state = loc, hdg
        if state in seen:
            return "loop"
        seen.add(state)
        if area.get(loc + hdg) == "#":
            hdg *= -1j
        loc += hdg
    return len(set(x[0] for x in seen))


a1 = solve(area)

a2 = 0
for k, v in area.items():
    if v == ".":
        result = solve(area, k)
        if result == "loop":
            a2 += 1

print_answers(a1, a2, day=6)
# 1473 low
