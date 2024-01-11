import re

import numpy as np
from utils import print_answers, read_file

DIRS = np.array([(0, 1), (1, 0), (0, -1), (-1, 0)])


class State:
    def __init__(self, pos: tuple[int]) -> None:
        self.pos = pos
        self.hdg = 0

    def copy(self):
        new = State(pos=self.pos)
        new.hdg = self.hdg
        return new

    def __repr__(self) -> str:
        return f"Pos {self.pos}, Facing: {self.hdg}"


def turn(st, dir):
    new = st.copy()
    d = (-1, 1)[dir == "R"]
    new.hdg = (new.hdg + d) % 4
    return new


def build_simple_warps(arr):
    warps = {}
    for i in range(arr.shape[0]):
        filled = np.where(arr[i, :] != " ")[0]
        a, b = (i, filled[0]), (i, filled[-1])
        warps[a, 2] = (b, 2)
        warps[b, 0] = (a, 0)

    for j in range(arr.shape[1]):
        filled = np.where(arr[:, j] != " ")[0]
        a, b = (filled[0], j), (filled[-1], j)
        warps[a, 3] = (b, 3)
        warps[b, 1] = (a, 1)
    return warps


def _rev(hdg):
    return (hdg + 2) % 4


def _create_warps(arr, cubes, hdgs, flip):
    cw = (arr != " ").sum(axis=1).min()  # cube width
    a = cw - 1  # addition if at cube's other end
    pairs = []
    sides = [hdgs[0], _rev(hdgs[1])]
    for c, side in zip(cubes, sides):
        br, bc = np.array(c) * cw
        match side:
            case 0:
                pairs.append([(br + i, bc + a) for i in range(cw)])
            case 1:
                pairs.append([(br + a, bc + i) for i in range(cw)])
            case 2:
                pairs.append([(br + i, bc) for i in range(cw)])
            case 3:
                pairs.append([(br, bc + i) for i in range(cw)])
    w = {}
    if flip:
        pairs[1] = pairs[1][::-1]
    for a, b in zip(*pairs):
        w[(a, hdgs[0])] = (b, hdgs[1])
        w[(b, _rev(hdgs[1]))] = (a, _rev(hdgs[0]))
    return w


def build_cube_warps(arr, arrangement):
    warps = {}
    for cubes, hdgs, flip in arrangement:
        warps.update(_create_warps(arr, cubes, hdgs, flip))
    return warps


def parse(raw_in):
    aa, bb = raw_in.split("\n\n")

    a = aa.split("\n")
    rows = max(len(x) for x in a)
    arr = np.zeros(shape=(len(a), rows), dtype="str")
    arr[:, :] = " "
    for i, row in enumerate(a):
        for j, c in enumerate(row):
            arr[i, j] = c

    cmds = re.findall(r"[\d]+|L|R", bb)
    cmds = [x if x in ("RL") else int(x) for x in cmds]

    return arr, cmds


def _get_start_pos(arr):
    a, b = np.where(arr == ".")
    return a[0], b[0]


def draw(arr, path):
    darr = arr.copy()
    for pos, hdg in path:
        v = ">v<^"[hdg]
        darr[pos] = v
    print("\n".join(map("".join, darr)))


def _get_next_pos_hdg(st, warps):
    simple = tuple(st.pos + DIRS[st.hdg])
    pos, hdg = warps.get((st.pos, st.hdg), (simple, st.hdg))
    return pos, hdg


def step(st, warps):
    new = st.copy()

    pos, hdg = _get_next_pos_hdg(st, warps)
    if arr[pos] == ".":
        new.pos = pos
        new.hdg = hdg
    return new


def get_password(st):
    return 1000 * (st.pos[0] + 1) + 4 * (st.pos[1] + 1) + st.hdg


def simulate(arr, cmds, warps):
    st = State(_get_start_pos(arr))

    path = [(st.pos, st.hdg)]
    for cmd in cmds:
        if isinstance(cmd, int):
            for _ in range(cmd):
                st = step(st, warps)
                path.append((st.pos, st.hdg))
        else:
            st = turn(st, cmd)

    return get_password(st)


# The arrangements are hard-coded for now,
# these should be inferred from arr instead
# (arrangement A is also incorrect)
ARRANGEMENT_A = [
    (((1, 2), (2, 3)), (0, 1), False),
    (((1, 1), (2, 2)), (1, 0), False),
    (((1, 1), (0, 2)), (3, 0), False),
    (((0, 2), (1, 0)), (3, 1), False),
    (((2, 2), (1, 0)), (1, 3), False),
    (((0, 2), (2, 3)), (0, 2), False),
    (((2, 3), (1, 0)), (1, 0), False),
]

ARRANGEMENT_B = [
    (((3, 0), (2, 1)), (0, 3), False),
    (((1, 1), (0, 2)), (0, 3), False),
    (((2, 0), (1, 1)), (3, 0), False),
    (((0, 1), (2, 0)), (2, 0), True),
    (((0, 1), (3, 0)), (3, 0), False),
    (((2, 1), (0, 2)), (0, 2), True),
    (((3, 0), (0, 2)), (1, 1), False),
]


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_22b.txt")
    arr, cmds = parse(raw_in)

    warps_simple = build_simple_warps(arr)
    warps_cube = build_cube_warps(arr, ARRANGEMENT_B)

    a1 = simulate(arr, cmds, warps_simple)
    a2 = simulate(arr, cmds, warps_cube)

    print_answers(a1, a2, day=22)
    # 66292
    # 127012
