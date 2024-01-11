from dataclasses import dataclass
from copy import deepcopy
from utils import read, print_answers


@dataclass
class Unit:
    type: str
    loc: complex
    hp: int = 200
    ap: int = 3


def parse(area):
    area = read(area).split("\n")
    floor = set()
    units = list()
    for y, r in enumerate(area):
        for x, c in enumerate(r):
            loc = x + y * 1j
            if c in "EG":
                units.append(Unit(c, loc, 200))
            if c != "#":
                floor.add(loc)
    return floor, units


def get_move(u, targets, units, floor):
    blocked = {x.loc for x in units}

    todo = [[u.loc]]
    seen = set()
    result = []
    while todo:
        _todo = []
        for path in todo:
            if path[-1] not in seen:
                seen.add(path[-1])
                for d in [-1j, -1, 1, 1j]:
                    nxt = path[-1] + d
                    if nxt in targets:
                        result.append(path)
                    elif (nxt in floor) and (nxt not in blocked):
                        _todo.append(path + [nxt])
        todo = _todo
        if result:
            best = sorted(result, key=lambda x: (x[-1].imag, x[-1].real))[0]
            if len(best) == 1:
                return u.loc
            else:
                return best[1]

    return u.loc


def get_target(u, units):
    targets = [t for t in units if (t.type != u.type) and (abs(t.loc - u.loc) == 1)]
    if targets:
        return sorted(targets, key=lambda t: (t.hp, t.loc.imag, t.loc.real))[0]


def get_result(units):
    eh = sum([u.hp for u in units if u.type == "E"])
    gh = sum([u.hp for u in units if u.type == "G"])
    return eh, gh


def simulate(floor, units, elf_ap=3, early_stop=False):
    units = deepcopy(units)
    if elf_ap != 3:
        for u in units:
            if u.type == "E":
                u.ap = elf_ap

    for i in range(1000):
        turns = sorted([*units], key=lambda x: (x.loc.imag, x.loc.real))

        for u in turns:
            if u in units:
                targets = {t.loc for t in units if t.type != u.type}
                if not targets:
                    eh, gh = get_result(units)
                    # print(f"Rounds {i} - elves hp: {eh} goblins hp: {gh}")
                    return i * max(eh, gh)
                u.loc = get_move(u, targets, units, floor)
                if t := get_target(u, units):
                    t.hp -= u.ap
                    if t.hp <= 0:
                        if early_stop and t.type == "E":
                            return -1
                        units.remove(t)


def find_threshold(floor, units):
    lo, hi = 3, 200
    while hi - lo > 1:
        mid = (lo + hi) // 2
        score = simulate(floor, units, mid, True)
        lo, hi = (lo, mid) if score >= 0 else (mid, hi)
    return simulate(floor, units, hi, True)


floor, units = parse("inputs/day_15b.txt")

a1 = simulate(floor, units)
a2 = find_threshold(floor, units)
print_answers(a1, a2, day=15)  # 221754 41972
