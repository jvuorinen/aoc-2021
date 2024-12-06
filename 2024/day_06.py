from utils import read, print_answers

raw = read().split('\n')
area = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}

def run(area, additional_obs=None):
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
        while area.get(loc + hdg) == "#":
            hdg *= -1j
        loc += hdg
    return len(set(x[0] for x in seen))


a1 = run(area)

empty = [k for k, v in area.items() if v == '.']
a2 = [run(area, x) for x in empty].count("loop")

print_answers(a1, a2, day=6)
