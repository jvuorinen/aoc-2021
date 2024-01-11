import numpy as np
from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_04.txt", split_delimiter="\n\n")
    nums = np.array([int(i) for i in raw_in[0].split(",")])

    parse_board = lambda b: [[int(x) for x in r.split()] for r in b.split("\n")]
    boards = [np.array(parse_board(b)) for b in raw_in[1:]]
    return nums, boards


def has_won(bool_board):
    row_wins = any(bool_board.prod(axis=1))
    col_wins = any(bool_board.prod(axis=0))
    return row_wins | col_wins


def yield_winner_scores(nums, boards):
    bool_boards = [np.zeros_like(b, dtype=bool) for b in boards]
    not_yet_won = set(range(len(bool_boards)))

    for num in nums:
        won_this_round = set()

        for i in not_yet_won:
            new_mark = boards[i] == num
            bool_boards[i] |= new_mark

            if has_won(bool_boards[i]):
                won_this_round.add(i)
                score = num * (boards[i] * ~bool_boards[i]).sum().sum()
                yield score

        not_yet_won -= won_this_round


if __name__ == "__main__":
    nums, boards = get_cleaned_input()

    scores = [s for s in yield_winner_scores(nums, boards)]

    print(f"Part 1 answer: {scores[0]}")
    print(f"Part 2 answer: {scores[-1]}")
