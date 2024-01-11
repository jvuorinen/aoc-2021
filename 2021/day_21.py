from functools import partial
from itertools import cycle, product
from collections import Counter

from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_21.txt")
    return [int(raw_in[0][-1]), int(raw_in[1][-1])]


def step_generic(turn, positions, scores, die_result, rules):
    """Given a state and a die result, return the next state. Create
    a game-specific partial function of this with given rules"""

    nxt_t = (turn + 1) % 2

    nxt_p = (positions[turn] - 1 + die_result) % rules["BOARD_LENGTH"] + 1
    p = list(positions)
    p[turn] = nxt_p

    s = list(scores)
    s[turn] += p[turn]

    victory = [0, 0]
    if s[turn] >= rules["SCORE_LIMIT"]:
        victory[turn] += 1

    return (nxt_t, tuple(p), tuple(s), tuple(victory))


def solve_1(start_a, start_b):
    RULES = {
        "ROLLS_PER_TURN": 3,
        "DIE_MAX": 20,
        "BOARD_LENGTH": 10,
        "SCORE_LIMIT": 1000,
    }

    step = partial(step_generic, rules=RULES)

    turn = 0
    positions = (start_a, start_b)
    scores = (0, 0)
    die = cycle(range(1, RULES["DIE_MAX"] + 1))
    rolls = 0

    while True:
        rolls += RULES["ROLLS_PER_TURN"]
        d = next(die) + next(die) + next(die)
        turn, positions, scores, victories = step(turn, positions, scores, d)
        if max(victories) > 0:
            return min(scores) * rolls


def _get_roll_counts(rules):
    """Helper function for getting possible
    roll results and their counts"""

    single_roll = [x for x in range(1, rules["DIE_MAX"] + 1)]
    all_rolls = [single_roll for _ in range(rules["ROLLS_PER_TURN"])]
    results = [sum(x) for x in product(*all_rolls)]
    c = Counter(results)
    return c


def _get_searchable_states(rules):
    """Helper function returning a generator yielding
    states to search in correct order"""

    p = product(range(1, rules["BOARD_LENGTH"] + 1), range(1, rules["BOARD_LENGTH"] + 1))

    s_unsorted = product(range(rules["SCORE_LIMIT"]), range(rules["SCORE_LIMIT"]))

    score_sorter = lambda t: sum(t) + 0.1 * min(t)
    s = sorted(s_unsorted, key=score_sorter)[::-1]

    n_s = ((n, s) for s, n in product(s, [0, 1]))
    n_p_s = ((n, p, s) for (n, s), p in product(n_s, p))

    return n_p_s


def solve_2(start_a, start_b):
    """Count odds starting from an almost
    finished game backwards to the start"""

    RULES = {
        "ROLLS_PER_TURN": 3,
        "DIE_MAX": 3,
        "BOARD_LENGTH": 10,
        "SCORE_LIMIT": 21,
    }

    step = partial(step_generic, rules=RULES)
    roll_counts = _get_roll_counts(RULES)
    states = _get_searchable_states(RULES)

    eventualities = {}

    for st in states:
        victories = [0, 0]
        for r, c in roll_counts.items():
            nxt_t, nxt_p, nxt_s, nxt_v = step(*st, r)
            if max(nxt_v) == 1:
                vic_a, vic_b = nxt_v
            else:
                vic_a, vic_b = eventualities[(nxt_t, nxt_p, nxt_s)]
            victories[0] += c * vic_a
            victories[1] += c * vic_b
        eventualities[st] = victories

    odds = eventualities[(0, (start_a, start_b), (0, 0))]
    return max(odds)


if __name__ == "__main__":
    start_a, start_b = get_cleaned_input()

    answer_1 = solve_1(start_a, start_b)
    answer_2 = solve_2(start_a, start_b)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
