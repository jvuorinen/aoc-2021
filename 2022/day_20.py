from utils import read_file, print_answers
import numpy as np


def step(arr, v, n):
    idx = np.argmax(arr == v)
    arr = np.roll(arr, -idx)
    rest = arr[1:]
    rest_rolled = np.roll(rest, -n)
    arr[1:] = rest_rolled
    return arr


def mix(code, times):
    moves = [(i, n) for n, i in zip(code, np.arange(len(code)))]

    arr = np.arange(len(code))
    for _ in range(times):
        for i, n in moves:
            arr = step(arr, i, n)
    return code[arr]


def get_coords(code):
    (ix,) = np.where(code == 0)
    idxs = (ix + np.array([1000, 2000, 3000])) % len(code)
    return code[idxs].sum()


def solve(code, key, times):
    code = key * code
    mixed = mix(code, times)
    return get_coords(mixed)


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_20b.txt").split()
    code = np.array(list(map(int, raw_in)))

    a1 = solve(code, key=1, times=1)
    a2 = solve(code, key=811589153, times=10)

    print_answers(a1, a2, day=20)
