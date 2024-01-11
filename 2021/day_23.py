import numpy as np
from tqdm import tqdm

from utils import read_input, memoize


def add_coords(c1: tuple, c2: tuple):
    return (c1[0] + c2[0], c1[1] + c2[1])


@memoize
def get_neighbor_coords(c: tuple):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = [add_coords(c, offset) for offset in offsets]
    return neighbors


class GameState:
    def __init__(self, size, positions=None) -> None:
        self.size = size

        self.rooms = {
            (2, 3): "A",
            (3, 3): "A",
            (2, 5): "B",
            (3, 5): "B",
            (2, 7): "C",
            (3, 7): "C",
            (2, 9): "D",
            (3, 9): "D",
        }
        if size == "big":
            self.rooms |= {
                (4, 3): "A",
                (5, 3): "A",
                (4, 5): "B",
                (5, 5): "B",
                (4, 7): "C",
                (5, 7): "C",
                (4, 9): "D",
                (5, 9): "D",
            }

        self.doorways = set([(1, 3), (1, 5), (1, 7), (1, 9)])

        if positions != None:
            self._positions = positions
            self.reset()

    def reset(self):
        self.choke_points = {
            (2, 3),
            (2, 5),
            (2, 7),
            (2, 9),
        }
        if self.size == "big":
            self.choke_points |= {
                (3, 3),
                (4, 3),
                (3, 5),
                (4, 5),
                (3, 7),
                (4, 7),
                (3, 9),
                (4, 9),
            }

        self.energy = 0
        self.unoccupied = set(self._positions["."])
        self.bugs = set()
        self.bugs |= set(("A", loc, 2) for loc in self._positions["A"])
        self.bugs |= set(("B", loc, 2) for loc in self._positions["B"])
        self.bugs |= set(("C", loc, 2) for loc in self._positions["C"])
        self.bugs |= set(("D", loc, 2) for loc in self._positions["D"])
        self.has_moved = set()
        self.outcome = 0  # -1 lose / 0 tbd / 1 win
        self.history = []

    def __repr__(self) -> str:
        SHAPE = (5, 13) if self.size == "small" else (7, 13)

        arr = np.full(SHAPE, fill_value="#")
        arr[tuple(zip(*self.unoccupied))] = "."

        for type, loc, _ in self.bugs:
            arr[loc] = type

        s = "\n".join(["".join(list(line)) for line in arr])
        s += f"\nEnergy: {self.energy}\nOutcome: {self.outcome}"
        return s

    def is_legal_destination(self, bug, destination):
        if destination in self.choke_points:
            return False

        bug_type, _, moves_left = bug
        room_type = self.rooms.get(destination)

        if bug_type == room_type:
            return True
        elif (moves_left == 2) and (room_type == None):
            if destination in self.doorways:
                return False
            else:
                return True
        else:
            return False

    def get_possible_actions(self):
        bugs_with_moves = [b for b in self.bugs if (b[-1] > 0)]
        moves = []
        for b in bugs_with_moves:
            for m in _get_possible_moves(self, b):
                # Optimisation: If possible to go
                # straight to a room, then always do it.
                if m[0] in self.rooms:
                    return [(b, m)]
                else:
                    moves.append((b, m))
        return moves

    def replay(self):
        cp = get_copy(self)
        cp.reset()

        for action in self.history:
            cp = step(cp, action)
            print()
            print(cp)


def _get_possible_moves(state: GameState, bug: tuple):
    visited = set()
    initial = bug[1]
    to_visit = {(initial, 0)}
    legit = set()

    while to_visit:
        current, dist = to_visit.pop()
        visited.add(current)
        if (dist > 1) and state.is_legal_destination(bug, current):
            # Optimisation: If possible to go
            # straight to a room, then always do it.
            if current in state.rooms:
                return [(current, dist)]
            legit.add((current, dist))
        for n in get_neighbor_coords(current):
            if (n in state.unoccupied) and (n not in visited):
                to_visit.add((n, dist + 1))

    return legit


def get_copy(state: GameState):
    new = GameState(size=state.size)
    new.energy = state.energy
    new.unoccupied = state.unoccupied.copy()
    new.bugs = state.bugs.copy()
    new.choke_points = state.choke_points.copy()
    new._positions = state._positions
    new.history = state.history[:]
    new.outcome = state.outcome

    return new


def calculate_score(bug_type, dist):
    m = {
        "A": 1,
        "B": 10,
        "C": 100,
        "D": 1000,
    }[bug_type]
    return m * dist


def determine_outcome(state):
    bugs = list(state.bugs)
    won_bugs = [(state.rooms.get(loc) == bt) for bt, loc, _ in bugs]
    moves_left = [x for _, _, x in bugs]

    if any(ml == 0 and not won for ml, won in zip(moves_left, won_bugs)):
        return -1

    if all(won_bugs):
        return 1

    return 0


def step(state: GameState, action: tuple):
    new = get_copy(state)

    new.history.append(action)

    (bug_type, loc_old, moves_left), (loc_new, dist) = action
    new.bugs.remove((bug_type, loc_old, moves_left))
    new.bugs.add((bug_type, loc_new, moves_left - 1))

    if loc_new in [(3, 3), (4, 3), (5, 3)]:
        new.choke_points -= {(loc_new[0] - 1, 3)}
    elif loc_new in [(3, 5), (4, 5), (5, 5)]:
        new.choke_points -= {(loc_new[0] - 1, 5)}
    elif loc_new in [(3, 7), (4, 7), (5, 7)]:
        new.choke_points -= {(loc_new[0] - 1, 7)}
    elif loc_new in [(3, 9), (4, 9), (5, 9)]:
        new.choke_points -= {(loc_new[0] - 1, 9)}

    elif (loc_old not in new.choke_points) and loc_old in [(3, 3), (4, 3), (5, 3)]:
        new.choke_points |= {(loc_new[0] - 1, 3)}
    elif (loc_old not in new.choke_points) and loc_old in [(3, 5), (4, 5), (5, 5)]:
        new.choke_points |= {(loc_new[0] - 1, 5)}
    elif (loc_old not in new.choke_points) and loc_old in [(3, 7), (4, 7), (5, 7)]:
        new.choke_points |= {(loc_new[0] - 1, 7)}
    elif (loc_old not in new.choke_points) and loc_old in [(3, 9), (4, 9), (5, 9)]:
        new.choke_points |= {(loc_new[0] - 1, 9)}

    new.unoccupied.add(loc_old)
    new.unoccupied.remove(loc_new)

    new.energy += calculate_score(bug_type, dist)
    new.outcome = determine_outcome(new)
    return new


def get_cleaned_input():
    raw_in_small = read_input("inputs/day_23.txt")

    raw_in_big = raw_in_small[:]
    raw_in_big.insert(3, "  #D#B#A#C#  ")
    raw_in_big.insert(3, "  #D#C#B#A#  ")

    arr_small = np.array(list(map(list, raw_in_small)))
    arr_big = np.array(list(map(list, raw_in_big)))

    positions_small = {
        ".": [(i, j) for i, j in zip(*np.where(arr_small == "."))],
        "A": [(i, j) for i, j in zip(*np.where(arr_small == "A"))],
        "B": [(i, j) for i, j in zip(*np.where(arr_small == "B"))],
        "C": [(i, j) for i, j in zip(*np.where(arr_small == "C"))],
        "D": [(i, j) for i, j in zip(*np.where(arr_small == "D"))],
    }

    positions_big = {
        ".": [(i, j) for i, j in zip(*np.where(arr_big == "."))],
        "A": [(i, j) for i, j in zip(*np.where(arr_big == "A"))],
        "B": [(i, j) for i, j in zip(*np.where(arr_big == "B"))],
        "C": [(i, j) for i, j in zip(*np.where(arr_big == "C"))],
        "D": [(i, j) for i, j in zip(*np.where(arr_big == "D"))],
    }

    state_small = GameState("small", positions_small)
    state_big = GameState("big", positions_big)

    return state_small, state_big


def find_solutions(state, book_keeping):
    if state.energy >= book_keeping["min_energy"]:
        book_keeping["n_early_stops"] += 1
    elif state.outcome == 1:
        book_keeping["solution_updates"] += 1
        book_keeping["min_energy"] = state.energy
        book_keeping["solution"] = state
        # print(book_keeping)
    elif state.outcome == -1:
        book_keeping["n_dead_ends"] += 1
    elif state.outcome == 0:
        actions = state.get_possible_actions()
        if len(actions) == 0:
            book_keeping["n_dead_ends"] += 1
        else:
            for a in actions:
                child = step(state, a)
                find_solutions(child, book_keeping)


def solve_exhaustive(state):
    book_keeping = {
        "n_early_stops": 0,
        "n_dead_ends": 0,
        "min_energy": 999_999,
        "solution_updates": 0,
        "solution": None,
    }

    # Doing children by children just to get tqdm
    actions = state.get_possible_actions()
    for a in tqdm(actions, ascii=True, ncols=80):
        child = step(state, a)
        find_solutions(child, book_keeping)

    return book_keeping


def play_randomly(state):
    if state.outcome != 0:
        return state
    else:
        actions = state.get_possible_actions()
        if actions:
            child = step(state, actions[0])
            state = play_randomly(child)

        return state


if __name__ == "__main__":
    state_small, state_big = get_cleaned_input()

    book_keep_small = solve_exhaustive(state_small)
    book_keep_big = solve_exhaustive(state_big)

    answer_1 = book_keep_small["min_energy"]
    answer_2 = book_keep_big["min_energy"]

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
