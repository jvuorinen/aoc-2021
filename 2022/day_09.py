from utils import read_file, print_answers
import numpy as np


def parse_moves(raw_in):
    DIRS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    res = []
    for r in raw_in:
        a, b = r.split(" ")
        res.extend(int(b) * [DIRS[a]])
    return res


def get_tail_update(h, t):
    diff = h - t
    is_diag = tuple(abs(diff)) == (1, 1)
    update = np.array([0, 0])
    if sum(abs(diff)) >= 2 and not is_diag:
        update += np.clip(diff, -1, 1)
    return update


def solve(moves, worm_len):
    rope = [np.array((0, 0)) for _ in range(worm_len)]
    rec = set([tuple(rope[-1])])
    for m in moves:
        rope[0] += m
        for i in range(len(rope) - 1):
            upd = get_tail_update(rope[i], rope[i + 1])
            if tuple(upd) == (0, 0):
                break
            rope[i + 1] += upd
        rec.add(tuple(rope[-1]))
    return len(rec)


if __name__ == "__main__":
    raw_in = read_file("inputs/day_09b.txt").split("\n")

    moves = parse_moves(raw_in)

    a1 = solve(moves, worm_len=2)
    a2 = solve(moves, worm_len=10)

    print_answers(a1, a2, day=9)
