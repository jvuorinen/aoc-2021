from collections import defaultdict
from utils import read_input
from dataclasses import dataclass


def get_graph_from_input():
    raw_in = read_input("inputs/day_12.txt")
    graph = defaultdict(set)
    for x in raw_in:
        a, b = x.split("-")
        graph[a].add(b)
        if b != "end":
            graph[b].add(a)
    return graph


@dataclass
class State:
    current: str
    history: list[str]
    visited_small: set[str]
    double_visit_allowed: bool
    success: bool


def create_initial_state():
    state = State(
        current="start",
        history=["start"],
        visited_small={"start"},
        double_visit_allowed=False,
        success=False,
    )
    return state


def get_possible_actions(state, graph):
    actions = graph[state.current].copy() - {"start"}

    if not state.double_visit_allowed:
        actions -= state.visited_small

    return actions


def step(state, action):
    """Returns a copy of state after taking action"""
    nxt = State(
        current=action,
        history=state.history.copy() + [action],
        visited_small=state.visited_small.copy(),
        double_visit_allowed=state.double_visit_allowed,
        success=False,
    )

    if action == "end":
        nxt.success = True

    elif action.islower():
        if action in nxt.visited_small:
            nxt.double_visit_allowed = False
        nxt.visited_small.add(action)

    return nxt


def find_solutions(state, graph):
    unexplored = [state]
    successes = []

    while unexplored:
        st = unexplored.pop()

        possible_actions = get_possible_actions(st, graph)
        child_states = [step(st, a) for a in possible_actions]

        for c in child_states:
            if c.success:
                successes.append(",".join(c.history))
            else:
                unexplored.append(c)

    return successes


def solve_1(graph):
    state = create_initial_state()

    solutions = find_solutions(state, graph)
    return solutions


def solve_2(graph):
    state = create_initial_state()
    state.double_visit_allowed = True

    solutions = find_solutions(state, graph)
    return solutions


if __name__ == "__main__":
    graph = get_graph_from_input()

    solutions_1 = solve_1(graph)
    solutions_2 = solve_2(graph)

    print(f"Part 1 answer: {len(solutions_1)}")
    print(f"Part 2 answer: {len(solutions_2)}")
