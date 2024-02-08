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
    prev_e: int = 0
    predecessor: Optional['State'] = None

    def get_token(self):
        locs = {x: i for i, f in enumerate(self.floors) for x in f}
        substances = set(x[:2] for x in locs.keys())
        # return tuple([self.e, self.prev_e] + sorted((locs[f"{s}-g"], locs[f"{s}-m"]) for s in substances))
        return tuple([self.e] + sorted((locs[f"{s}-g"], locs[f"{s}-m"]) for s in substances))
        # return tuple([self.e] + [frozenset(s) for s in self.floors])

    def copy(self):
        return State(e=self.e, floors=[x.copy() for x in self.floors], i=self.i, prev_e = self.e, predecessor=self)

    def get_score(self):
        s = 0
        for i, f in enumerate(self.floors, 1):
            for x in f:
                s += i*(1 if x[-1] == 'm' else 0.9)
        return s
        # return sum(i*len(f) for i, f in enumerate(self.floors))

    def get_n_items(self):
        return len(set.union(*self.floors))

    def __hash__(self) -> int:
        return hash(self.get_token())

    def __eq__(self, other):
        if isinstance(other, State):
            return hash(self) == hash(other)
        return False
    

def parse(raw):
    def shorten(s):
        ws = s.split(' ')
        return f"{ws[0][:2]}-{ws[1][0]}"
    floors = [set(map(shorten, re.findall(r'[^ ]+ (?:microchip|generator)', x))) for x in raw]
    return State(e=0, floors=floors)


def floor_ok(f):
    chips = set(x[:2] for x in f if x[-1] =='m')
    gens = set(x[:2] for x in f if x[-1] =='g')
    unprotected = chips - gens
    return not (len(unprotected) > 0 and len(gens) > 0)


def get_children(state):
    current = state.floors[state.e]
    carry = [set([x]) for x in current] + [*map(set, combinations(current, 2))]
    res = []
    for cr in carry:
        candidate = current - cr
        if floor_ok(candidate):
            floors = [nxt for d in (-1, 1) if 0 <= (nxt := state.e + d) <= 3]
            for f in floors:
                dest = state.floors[f]
                candidate = dest | cr
                if floor_ok(candidate):
                    st = state.copy()
                    st.e = f
                    st.prev_e = state.e
                    st.floors[state.e] -= cr
                    st.floors[f] |= cr
                    st.i += 1
                    res.append(st)
    return res


def solve(st, extras=False):
    st = st.copy()
    if extras:
        st.floors[0] |= {'el-g', 'el-m', 'di-g', 'di-m'}

    n_items = st.get_n_items()

    todo = [st]
    seen = set()
    for _ in range(200):
        _rnd = set()
        for st in todo:
            if len(st.floors[3]) == n_items:
                return st.i
            seen.add(st)
            for _st in get_children(st):
                if _st not in seen:
                    _rnd.add(_st)
        todo = sorted(_rnd, key=lambda x: x.get_score(), reverse=True)

raw = read(2016, 11).split("\n")
st = parse(raw)

a1 = solve(st)
a2 = solve(st, extras=True)

print_answers(a1, a2, day=11)  # 31 51
