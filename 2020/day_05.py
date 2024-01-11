from itertools import count

from utils import read_input


def get_cleaned_input():
    res = [x for x in read_input("inputs/day_05.txt")]
    return res


def get_sequences(bpass):
    row, col = [], []
    for c in bpass:
        if c == "F":
            row.append(0)
        if c == "B":
            row.append(1)
        if c == "L":
            col.append(0)
        if c == "R":
            col.append(1)
    return row, col


def calculate_place(sequence, max_value):
    res = 0
    halfway = max_value / 2
    for x in sequence:
        res += x * halfway
        halfway /= 2
    return int(res)


def get_seat_id(row, col):
    return row * 8 + col


def parse_boarding_pass(bpass):
    row_seq, col_seq = get_sequences(bpass)

    row = calculate_place(row_seq, 128)
    col = calculate_place(col_seq, 8)
    seat_id = get_seat_id(row, col)
    return row, col, seat_id


def solve_1(passes):
    res = max(parse_boarding_pass(p)[2] for p in passes)
    return res


def solve_2(passes):
    ids = sorted(parse_boarding_pass(p)[2] for p in passes)
    for a, b in zip(ids, count(ids[0])):
        if a != b:
            return b


if __name__ == "__main__":
    passes = get_cleaned_input()

    answer_1 = solve_1(passes)
    answer_2 = solve_2(passes)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
