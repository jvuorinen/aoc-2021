import numpy as np
from utils import add_coords, get_neighbors, print_answers, read_file

DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

NEXT_HDG = {
    "> -": ">",
    "> 7": "v",
    "> J": "^",
    "< -": "<",
    "< F": "v",
    "< L": "^",
    "^ |": "^",
    "^ 7": "<",
    "^ F": ">",
    "v |": "v",
    "v J": "<",
    "v L": ">",
}


def step(state, area):
    loc, hdg = state
    _loc = add_coords(loc, DIRS[hdg])
    _hdg = NEXT_HDG.get(f"{hdg} {area[_loc]}")
    if _hdg:
        return (_loc, _hdg)


def find_path(state, area):
    path = [state]
    while (state := step(state, area)) and (state != path[0]):
        path.append(state)
    return path


def calculate_inside_size(path):
    # Increase resolution
    path_double_res = set([])
    for loc, hdg in path:
        _loc = int(loc[0] * 2), int(loc[1] * 2)
        interpolated = add_coords(_loc, DIRS[hdg])
        path_double_res |= {_loc, interpolated}

    # Flood fill to get the inside locs
    Q = [(140, 140)]  # Hard coded the start, this has to be on the inside
    visited = set()
    while Q:
        x = Q.pop()
        visited.add(x)
        Q.extend([n for n in get_neighbors(x) if (n not in path_double_res) and (n not in visited)])
    original_res = [(int(a / 2), int(b / 2)) for a, b in visited if (a % 2 == 0 and b % 2 == 0)]
    return len(original_res)


if __name__ == "__main__":
    area = np.array([list(x) for x in read_file("inputs/day_10b.txt").split("\n")])

    start = tuple([x[0] for x in tuple(np.where(area == "S"))])
    path = max([find_path((start, hdg), area) for hdg in list("^v<>")], key=len)

    a1 = len(path) // 2
    a2 = calculate_inside_size(path)

    print_answers(a1, a2, day=10)  # Correct: 7173, 291
