import numpy as np
from utils import read_file, print_answers


def get_load(arr):
    scores = (np.arange(len(arr)) + 1)[::-1]
    return sum(scores * (arr == "O").sum(axis=1))


def get_free_rocks(arr):
    rocks = zip(*np.where(arr == "O"))
    return [(i, j) for i, j in rocks if i > 0 and arr[i - 1, j] == "."]


def tilt(arr):
    arr = arr.copy()
    while free := get_free_rocks(arr):
        for i, j in free:
            arr[i, j] = "."
            arr[i - 1, j] = "O"
    return arr


def spin(arr):
    for _ in range(4):
        arr = tilt(arr)
        arr = np.rot90(arr, -1)
    return arr


def determine_behaviour(arr):
    nums = []
    tokens = []
    while True:
        t = tuple((arr == "O").flatten())
        if t in tokens:
            cycle_start = tokens.index(t)
            return nums[:cycle_start], nums[cycle_start:]
        tokens.append(t)
        nums.append(get_load(arr))
        arr = spin(arr)


def get_load_after_spinning(arr, n):
    head, cycle = determine_behaviour(arr)
    mod = (n - len(head)) % len(cycle)
    return cycle[mod]


if __name__ == "__main__":
    raw_in = read_file("inputs/day_14b.txt").split()
    arr = np.array([list(x) for x in raw_in])

    a1 = get_load(tilt(arr))
    a2 = get_load_after_spinning(arr, 1000000000)

    print_answers(a1, a2, day=14)  # Correct: 105003, 93742
