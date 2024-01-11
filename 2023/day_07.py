from collections import Counter
from utils import print_answers, read_file

ORDER_1 = "23456789TJQKA"
ORDER_2 = "J23456789TQKA"


def get_strength(hand, use_joker=False):
    original = hand
    if use_joker:
        hand = replace_joker(hand)
    counts = list(Counter(hand).values())
    score = max(counts)
    if (score == 3 and 2 in counts) or counts.count(2) == 2:
        score += 0.5
    card_scores = ORDER_2 if use_joker else ORDER_1
    return [score] + [card_scores.find(x) for x in original]


def replace_joker(hand):
    candidates = [hand.replace("J", x) for x in ORDER_1]
    return max(candidates, key=get_strength)


def solve(hands, str_func):
    ranked = sorted(hands, key=str_func)
    return sum([i * int(x[1]) for i, x in enumerate(ranked, 1)])


raw_in = read_file("inputs/day_07b.txt").split("\n")
hands = [x.split() for x in raw_in]

a1 = solve(hands, str_func=lambda x: get_strength(x[0]))
a2 = solve(hands, str_func=lambda x: get_strength(x[0], use_joker=True))

print_answers(a1, a2, day=7)  # Correct: 250957639, 251515496
