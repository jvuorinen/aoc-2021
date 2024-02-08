import re
from itertools import combinations
from dataclasses import dataclass
from typing import Optional
from utils import read, print_answers


@dataclass
class State:
    e: int
    floors: list[set]
    i: int = 0
    predecessor: Optional["State"] = None

    def copy(self):
        return State(e=self.e, floors=[x.copy() for x in self.floors], i=self.i, predecessor=self)

    def get_n_items(self):
        return len(set.union(*self.floors))

    def __hash__(self) -> int:
        locs = {x: i for i, f in enumerate(self.floors) for x in f}
        substances = set(x[:2] for x in locs.keys())
        state = tuple([self.e] + sorted((locs[f"{s}-g"], locs[f"{s}-m"]) for s in substances))
        return hash(state)

    def __eq__(self, other):
        if isinstance(other, State):
            return hash(self) == hash(other)
        return False


def parse(raw):
    def shorten(s):
        ws = s.split(" ")
        return f"{ws[0][:2]}-{ws[1][0]}"

    floors = [set(map(shorten, re.findall(r"[^ ]+ (?:microchip|generator)", x))) for x in raw]
    return State(e=0, floors=floors)


def floor_ok(flr):
    chips = set(x[:2] for x in flr if x[-1] == "m")
    gens = set(x[:2] for x in flr if x[-1] == "g")
    unprotected = chips - gens
    return not (len(unprotected) > 0 and len(gens) > 0)


def get_children(state):
    current = state.floors[state.e]
    carry = [*map(set, set(combinations(current, 1)) | set(combinations(current, 2)))]
    for cr in carry:
        if floor_ok(current - cr):
            floors = [nxt for d in (-1, 1) if 0 <= (nxt := state.e + d) <= 3]
            for f in floors:
                dest = state.floors[f]
                if floor_ok(dest | cr):
                    st = state.copy()
                    st.e = f
                    st.prev_e = state.e
                    st.floors[state.e] -= cr
                    st.floors[f] |= cr
                    st.i += 1
                    yield st


def solve(st, extras=False):
    st = st.copy()
    if extras:
        st.floors[0] |= {"el-g", "el-m", "di-g", "di-m"}

    n_items = st.get_n_items()
    todo = [st]
    seen = set()
    while todo:
        rnd = set()
        for st in todo:
            if len(st.floors[3]) == n_items:
                return st.i
            seen.add(st)
            for _st in get_children(st):
                if _st not in seen:
                    rnd.add(_st)
        todo = [*rnd]


raw = read(2016, 11).split("\n")
st = parse(raw)

a1 = solve(st)
a2 = solve(st, extras=True)

print_answers(a1, a2, day=11)  # 31 51
