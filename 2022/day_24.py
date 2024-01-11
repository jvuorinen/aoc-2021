from math import lcm

import numpy as np
from utils import _add_coords, print_answers, read_file

DIRS = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


class State:
    def __init__(self, board, cycle, blizzards, bz_next, turnarounds) -> None:
        self.board = board
        self.blizzards = blizzards
        self.bz_next = bz_next
        self.turnarounds = turnarounds

        self.player = (0, 1)
        self.turn = 0
        self.goal = (board.shape[0] - 1, board.shape[1] - 2)
        self.next_goal = (0, 1)
        self.cycle = cycle

        self.movable = set(list(zip(*np.where(self.board == "."))))

    @property
    def turn_idx(self):
        return self.turn % self.cycle

    @property
    def at_goal(self):
        return self.player == self.goal

    @property
    def finished(self):
        return self.at_goal and (self.turnarounds == 0)

    @property
    def state_token(self):
        return (self.turn_idx, self.turnarounds, self.player)

    def _turn_or_finish(self):
        if self.turnarounds > 0:
            self.turnarounds -= 1
            self.goal, self.next_goal = self.next_goal, self.goal

    def __repr__(self):
        arr = self.board.copy()

        for bznxt in self.bz_next[self.turn_idx]:
            arr[bznxt] = ","
        for c, bset in self.blizzards.items():
            for b in bset:
                arr[b[self.turn_idx]] = c
        arr[self.player] = "E"

        s = f"Turn: {self.turn}\n"
        s += f"Turn idx: {self.turn_idx} - Cycle: {self.cycle}\n"
        s += f"turnarounds: {self.turnarounds}\n"
        s += f"Finished: {self.at_goal}\n"
        s += "\n".join(map("".join, arr))
        return s


def act(st, action):
    new = State(st.board, st.cycle, st.blizzards, st.bz_next, st.turnarounds)
    new.goal = st.goal
    new.next_goal = st.next_goal

    match action:
        case "U":
            new.player = _add_coords(st.player, DIRS["U"])
        case "D":
            new.player = _add_coords(st.player, DIRS["D"])
        case "L":
            new.player = _add_coords(st.player, DIRS["L"])
        case "R":
            new.player = _add_coords(st.player, DIRS["R"])
        case "w":
            new.player = st.player
    new.turn = st.turn + 1
    if new.at_goal:
        new._turn_or_finish()
    return new


def is_valid(c, st):
    if c not in st.movable:
        return False
    if c in st.bz_next[st.turn_idx]:
        return False
    return True


def get_actions(st):
    actions = []
    if is_valid(st.player, st):
        actions.append(("w", st.player))
    for k, v in DIRS.items():
        c = _add_coords(st.player, v)
        if is_valid(c, st):
            actions.append((k, v))
    return [x[0] for x in actions]


def create_initial_state(raw_in, turnarounds):
    arr = np.array([list(x) for x in raw_in.split()])

    _parse = lambda x, arr: list(map(tuple, zip(*np.where((arr == x)))))
    _roll = lambda lst, x: lst[lst.index(x) :] + lst[: lst.index(x)]
    _base_c = lambda c, s: [(i % s, c) for i in range(1, s - 1)]
    _base_r = lambda r, s: [(r, i % s) for i in range(1, s - 1)]
    _path_c = lambda t, s, d: _roll(_base_c(t[1], s)[::d], t)
    _path_r = lambda t, s, d: _roll(_base_r(t[0], s)[::d], t)

    sy, sx = arr.shape
    b_u = [_path_c(t, sy, -1) for t in _parse("^", arr)]
    b_d = [_path_c(t, sy, 1) for t in _parse("v", arr)]
    b_l = [_path_r(t, sx, -1) for t in _parse("<", arr)]
    b_r = [_path_r(t, sx, 1) for t in _parse(">", arr)]

    cycle = lcm(sy - 2, sx - 2)
    blizzards = {
        "^": [[b[i % len(b)] for i in range(cycle)] for b in b_u],
        "v": [[b[i % len(b)] for i in range(cycle)] for b in b_d],
        "<": [[b[i % len(b)] for i in range(cycle)] for b in b_l],
        ">": [[b[i % len(b)] for i in range(cycle)] for b in b_r],
    }

    bz_next = [set() for _ in range(cycle)]
    for bset in blizzards.values():
        for b in bset:
            for i in range(cycle):
                bz_next[i].add(b[(i + 1) % cycle])

    board = arr.copy()
    board[(board != "#") & (board != ".")] = "."

    st = State(board, cycle, blizzards, bz_next, turnarounds)
    return st


def solve(raw_in, turnarounds):
    st = create_initial_state(raw_in, turnarounds)

    visited = set([st.state_token])
    Q = [st]
    while Q:
        st = Q.pop(0)
        for a in get_actions(st):
            new = act(st, a)
            if new.finished:
                return st.turn
            if new.state_token not in visited:
                visited.add(new.state_token)
                Q.append(new)


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_24b.txt")

    a1 = solve(raw_in, 0)
    a2 = solve(raw_in, 2)

    print_answers(a1, a2, day=24)
