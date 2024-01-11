from dataclasses import dataclass
from copy import deepcopy
import re
from utils import read, print_answers


@dataclass
class Unit:
    team: int
    idx: int
    n: int
    hp: int
    weak: set[str]
    immune: set[str]
    atk: int
    atk_type: set[str]
    init: int


def parse(file):
    data = [x.split("\n")[1:] for x in read(file).split("\n\n")]
    units = []
    for team, lines in enumerate(data):
        for idx, line in enumerate(lines, 1):
            n, hp, atk, init = map(int, re.findall(r"\d+", line))
            atk_type = re.findall(r"([a-x]+) damage", line)[0]
            _weak = re.findall(r"weak to ([^;\)]*)", line)
            weak = set(_weak[0].split(", ")) if _weak else set()
            _immune = re.findall(r"immune to ([^;\)]*)", line)
            immune = set(_immune[0].split(", ")) if _immune else set()
            units.append(Unit(team, idx, n, hp, weak, immune, atk, atk_type, init))
    return units


def get_dmg(a, d):
    if a.atk_type in d.immune:
        return 0
    m = 2 if a.atk_type in d.weak else 1
    return m * a.n * a.atk


def get_counts(units):
    return [sum([x.n for x in units if x.team == t]) for t in (0, 1)]


def fight(units, boost=0):
    units = deepcopy(units)
    for u in units:
        if u.team == 0:
            u.atk += boost

    while all(result := get_counts(units)):
        ns = tuple([u.n for u in units])

        left = [u for u in units if u.n > 0]
        tgts = []
        for a in sorted(units, key=lambda u: (u.n * u.atk, u.init), reverse=True):
            possible = [
                (dmg, d.n * d.atk, d.init, d)
                for d in left
                if (a.team != d.team) and (dmg := get_dmg(a, d)) > 0
            ]
            if possible:
                *_, d = max(possible)
                left.remove(d)
                tgts.append((a, d))
        for a, d in sorted(tgts, key=lambda t: t[0].init, reverse=True):
            if a.n > 0:
                dmg = get_dmg(a, d)
                d.n = max(0, d.n - dmg // d.hp)
        if tuple([u.n for u in units]) == ns:
            return result
    return result


def find_boost(units):
    lo, hi = (0, 5000)
    while hi - lo > 1:
        v = (hi + lo) // 2
        res = fight(units, v)
        in_low = res[0] > 0 and res[1] == 0
        lo, hi = (lo, v) if in_low else (v, hi)
    return hi


units = parse("inputs/day_24b.txt")
a1 = fight(units)[1]

b = find_boost(units)
a2 = fight(units, b)[0]
print_answers(a1, a2, day=24)  # 21070, 7500
