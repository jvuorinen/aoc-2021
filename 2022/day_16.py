from utils import read_file, print_answers
import re
from dataclasses import dataclass, field
from typing import Optional, Any
from itertools import product


def parse(raw_in):
    expr = "Valve (..).*rate=([\d]+).*valve[s]* (.*)"
    rates = {}
    links = {}
    for r in raw_in:
        v, f, dst = re.findall(expr, r)[0]
        rates[v] = int(f)
        links[v] = sorted(dst.split(", "))
    return rates, links


@dataclass
class State:
    time: int = 1
    loc: tuple[str] = ("AA", "AA")
    opened: set[str] = field(default_factory=set)
    released: int = 0
    predecessor: Optional[Any] = None

    def get_progression(self):
        positions = tuple(sorted(self.loc))
        opened = tuple(sorted([x for x in self.opened]))
        token = (self.time, positions, opened)
        return token, self.released

    def __repr__(self):
        return f"t: {self.time}, loc: {self.loc}, open: {self.opened}, released: {self.released}"


@dataclass
class SimulationData:
    rates: dict
    links: dict
    n_rounds: int
    best_state: Optional[State] = None
    best_score: int = 0
    n_finishes: int = 0
    pr_lost_already: int = 0
    pr_mirror: int = 0
    pr_seen_better: int = 0
    pr_precalculated: int = 0
    progression: dict = field(default_factory=dict)

    def __repr__(self) -> str:
        s = "---Simulation data---\n"
        s += f"best score: {self.best_score}\n"
        s += f"n. finishes: {self.n_finishes}\n"
        s += f"n. prunings-lost-already: {self.pr_lost_already}\n"
        s += f"n. prunings-mirror: {self.pr_mirror}\n"
        s += f"n. prunings-seen-better: {self.pr_seen_better}\n"
        s += f"n. prunings-precalculated: {self.pr_precalculated}\n"
        return s


def calculate_release(st, data: SimulationData):
    return sum([data.rates[v] for v in st.opened])


def act(st: State, cmd: tuple[str, str], data: SimulationData):
    new = State(
        st.time + 1,
        st.loc,
        st.opened.copy(),
        st.released,
    )

    new.predecessor = st

    newloc = list(st.loc)
    for i, p_cmd in enumerate(cmd):
        match p_cmd:
            case "move", dst:
                newloc[i] = dst
            case "open", valve:
                new.opened.add(valve)
    new.loc = tuple(newloc)
    new.released += calculate_release(new, data)
    return new


def prune_redundant(actions, st, data):
    s = set()
    res = []
    for a in actions:
        tag = tuple(sorted(a))
        if tag not in s:
            s.add(tag)
            res.append(a)
        else:
            data.pr_mirror += 1
    return res


def get_children(st: State, data: SimulationData):
    players = ([], [])

    if data.n_players == 1:
        players[1].append(("wait",))

    for i in range(data.n_players):
        if len(st.opened) < data.n_valves:
            loc = st.loc[i]
            if (st.loc[i] not in st.opened) and (rates[loc] != 0):
                players[i].append(("open", loc))

            for dst in links[loc]:
                if (st.predecessor) and (dst == st.predecessor.loc[i]):
                    continue
                players[i].append(("move", dst))

        if len(players[i]) == 0:
            players[i].append(("wait",))

    actions = [(p1, p2) for p1, p2 in product(*players)]
    actions = prune_redundant(actions, st, data)

    states = [act(st, a, data) for a in actions]
    return states


def check_bad_potential(st, data: SimulationData):
    time_left = data.n_rounds - st.time
    if len(st.opened) == data.n_valves:
        potential = st.released + time_left * calculate_release(st, data)
    else:
        potential = st.released + time_left * sum(list(data.rates.values()))
    return potential < max(data.potential_threshold, data.best_score)


def hustle(st, data: SimulationData):
    if st.time == data.n_rounds:
        data.n_finishes += 1
        if st.released > data.best_score:
            data.best_state = st
            data.best_score = st.released
    elif len(st.opened) == data.n_valves:
        data.pr_precalculated += 1

        time_left = data.n_rounds - st.time
        result = st.released + time_left * sum(list(data.rates.values()))
        if result > data.best_score:
            data.best_state = st
            data.best_score = result
    else:
        children = get_children(st, data)
        for new in children:
            if check_bad_potential(new, data):
                data.pr_lost_already += 1
                return
            else:
                token, p = new.get_progression()
                if (token not in data.progression) or (p > data.progression[token]):
                    data.progression[token] = p
                    hustle(new, data)
                else:
                    data.pr_seen_better += 1


def describe(st):
    path = [st]
    while st.predecessor:
        st = st.predecessor
        path.append(st)
    return path[::-1]


def solve(rates, links, n_players, n_rounds, potential_threshold):
    data = SimulationData(rates, links, n_rounds)
    data.potential_threshold = potential_threshold
    data.n_players = n_players
    data.n_valves = sum([1 for v in data.rates.values() if v != 0])
    st = State()

    hustle(st, data)
    return data.best_score


if __name__ == "__main__":
    raw_in = read_file("inputs/day_16b.txt").split("\n")
    rates, links = parse(raw_in)

    # Part 2 is still slow, around 8 min...
    a1 = solve(rates, links, n_players=1, n_rounds=30, potential_threshold=1000)
    a2 = solve(rates, links, n_players=2, n_rounds=26, potential_threshold=2000)

    print_answers(a1, a2, day=16)
