import re
from dataclasses import dataclass
from random import shuffle
from typing import Optional

import numpy as np
from tqdm import tqdm

from utils import print_answers, read_file

np.seterr(divide="ignore")

PRODS = [np.roll(np.array([1, 0, 0, 0]), a) for a in range(4)]


def parse_blueprint(line):
    ORDER = ["ore", "clay", "obsidian", "geode"]

    get_prices = lambda x: {b: int(a) for a, b in re.findall("(\d+) (\w+)", x)}
    to_arr = lambda x: np.array([x.get(p, 0) for p in ORDER])

    _, instrs = line.split(":")
    prices = [get_prices(robo) for robo in instrs.split(".")][:4]
    return np.array([to_arr(p) for p in prices])


class State:
    def __init__(self) -> None:
        self.t = 0
        self.prod = np.array([1, 0, 0, 0])
        self.stash = np.array([0, 0, 0, 0])
        self.end_reached: bool = False

    def copy(self):
        new = State(self)
        new.t = self.t
        new.prod = self.prod
        new.stash = self.stash
        return new

    def __repr__(self):
        return f"t: {self.t}, prod: {self.prod}, stash: {self.stash}"


@dataclass
class SimulationData:
    limit: int
    prices: np.array
    best: Optional[State] = None
    best_score: int = 0
    finishes: int = 0
    prunings: int = 0
    progress = [0 for _ in range(25)]

    def __repr__(self) -> str:
        s = ""
        s += "== Simulation Data ==\n"
        s += f"best score: {self.best_score}\n"
        s += f"n.finishes: {self.finishes}\n"
        s += f"n.prunings: {self.prunings}\n"
        return s


def shuffled(t):
    tmp = list(t)
    shuffle(tmp)
    return tuple(tmp)


def max_potential_reached(st: State, data: SimulationData):
    return all(st.stash >= data.prices[3]) and all(st.prod >= data.prices[3])


def get_actions(st: State, data: SimulationData):
    if max_potential_reached(st, data):
        return [3]
    f = []
    if st.prod[0] > 0:
        f.extend([0, 1])
    if st.prod[1] > 0:
        f.append(2)
    if st.prod[2] > 0:
        f.append(3)
    return shuffled(f)


def ceildiv(a, b):
    return -1 * (-a // b)


def act(st: State, a: int, data: SimulationData):
    new = State()

    dp = data.prices[a] - st.stash
    if max(dp) <= 0:
        dt = 1
    else:
        dp // st.prod
        dt = ceildiv(dp, st.prod).max() + 1
        dt = min(dt, data.limit - st.t)
    new.t = st.t + dt
    new.stash = st.stash + dt * st.prod - data.prices[a]
    new.prod = st.prod + PRODS[a]
    if new.t >= data.limit:
        new.end_reached = True
    return new


def triangular(x):
    result = (x * (x + 1)) / 2
    return int(result)


def get_potential(st: State, data: SimulationData):
    dt = data.limit - st.t
    certain = st.stash[3] + dt * st.prod[3]

    tpot = dt if all(st.stash >= data.prices[3]) else dt - 1
    potential = triangular(tpot)
    return certain + potential


def play_randomly(st, data):
    for _ in range(6):
        a = get_actions(st)[0]
        st = act(st, a, data)
    return st


def play(st: State, data: SimulationData):
    if st.end_reached:
        data.finishes += 1
        if st.stash[3] > data.best_score:
            data.best_score = st.stash[3]
            data.best = st
    else:
        for a in get_actions(st, data):
            new = act(st, a, data)

            if get_potential(st, data) > data.best_score:
                play(new, data)
            else:
                data.prunings += 1


def run_simulation(blueprint, limit):
    data = SimulationData(limit=limit, prices=blueprint)
    st = State()
    play(st, data)
    return data


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_19b.txt").split("\n")
    blueprints = [parse_blueprint(r) for r in raw_in]

    # Not optimised, runs horribly slow

    # Part 1
    sims_1 = [run_simulation(bp, 24) for bp in tqdm(blueprints)]
    a1 = sum(i * (s.best_score) for i, s in enumerate(sims_1, 1))

    # Part 2
    sims_2 = [run_simulation(bp, 32) for bp in tqdm(blueprints[:3])]
    a2 = np.prod([x.best_score for x in sims_2])
    print(a2)

    print_answers(a1, a2, day=19)
    # 2341
    # 3689
