from itertools import cycle

import numpy as np
from tqdm import tqdm

from utils import *


def create_fft_matrix(n):
    initial = [0, 1, 0, -1]

    rows = []
    for i in range(n):
        it = cycle(x for x in initial for _ in range(i + 1))
        rows.append([next(it) for _ in range(n + 1)])
    arr = np.array(rows)[:, 1:]
    return arr


def solve_1(input_list):
    M = create_fft_matrix(len(input_list))
    v = np.array(input_list.copy())

    for _ in range(100):
        nxt = np.matmul(M, v)
        v = np.mod(abs(nxt), 10)

    answer = "".join(str(x) for x in v[:8])
    return answer


def get_initial_list(input_list, n_needed):
    it = cycle(input_list[::-1])
    res = []
    for _ in range(n_needed):
        x = next(it)
        res.append(x)
    return res


def do_tail_fft(input_tail):
    res = []
    s = 0
    for x in input_tail:
        s += x
        res.append(s % 10)
    return res


def solve_2(input_list):
    total_length = len(input_list) * 10000
    to_skip = int("".join(map(str, input_list[:7])))
    n_needed = total_length - to_skip

    todo = get_initial_list(input_list, n_needed)

    for _ in tqdm(range(100)):
        todo = do_tail_fft(todo)

    answer = "".join(str(x) for x in todo[::-1][:8])
    return answer


if __name__ == "__main__":
    raw_in = read_input("inputs/day_16.txt")
    input_list = [int(x) for x in list(raw_in[0])]

    answer_1 = solve_1(input_list)
    answer_2 = solve_2(input_list)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
