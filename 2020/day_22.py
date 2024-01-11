from itertools import count

from utils import read_input


def parse_input(raw_in):
    parse = lambda p: [int(x) for x in p.split(":")[1].split()]
    return [parse(p) for p in raw_in]


def regular_game(decks):
    while (len(decks[0]) > 0) & (len(decks[1]) > 0):
        a, a_ = decks[0][0], decks[0][1:]
        b, b_ = decks[1][0], decks[1][1:]
        decks = [a_ + [a, b], b_] if (a > b) else [a_, b_ + [b, a]]
    winner = 0 if len(decks[1]) == 0 else 1
    return decks, winner


def _tuplify(decks):
    return tuple(tuple(p) for p in decks)


def recursive_game(decks):
    history = set()
    while (len(decks[0]) > 0) & (len(decks[1]) > 0):
        # Failsafe
        t = _tuplify(decks)
        if t in history:
            return decks, 0
        else:
            history.add(t)

        # Determine round winner
        a, a_ = decks[0][0], decks[0][1:]
        b, b_ = decks[1][0], decks[1][1:]
        if (len(a_) < a) | (len(b_) < b):
            round_winner = 0 if (a > b) else 1
        else:
            _, round_winner = recursive_game([a_[:a], b_[:b]])

        # Update deck
        decks = [a_ + [a, b], b_] if (round_winner == 0) else [a_, b_ + [b, a]]

    game_winner = 0 if len(decks[1]) == 0 else 1
    return decks, game_winner


def solve(decks, play_func):
    decks, winner = play_func(decks)
    score = sum(m * c for m, c in zip(count(1), decks[winner][::-1]))
    return score


if __name__ == "__main__":
    raw_in = read_input("inputs/day_22.txt", split_delimiter="\n\n")
    decks = parse_input(raw_in)

    answer_1 = solve(decks, play_func=regular_game)
    answer_2 = solve(decks, play_func=recursive_game)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
