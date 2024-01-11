from utils import read_input
from itertools import count


def transform(n, loops):
    v = 1
    for _ in range(loops):
        v = v * n
        v = v % 20201227
    return v


def find_loops(pub):
    v = 1
    for ls in count(1):
        # print(v)
        v = v * 7
        v = v % 20201227
        if v == pub:
            return ls


def solve_1(pub_c, pub_d):
    loops_c = find_loops(pub_c)
    # loops_d = find_loops(pub_d)

    encr_key = transform(pub_d, loops_c)
    return encr_key


if __name__ == "__main__":
    pub_c, pub_d = [int(i) for i in read_input("inputs/day_25.txt")]

    answer_1 = solve_1(pub_c, pub_d)

    print(f"Part 1 answer: {answer_1}")
