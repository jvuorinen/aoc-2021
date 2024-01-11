from utils import read_input, memoize


def get_cleaned_input():
    start, tmp = read_input("inputs/day_14.txt", "\n\n")

    raw = [tuple(x.split(" -> ")) for x in tmp.split("\n")]
    mapping = {a: b for a, b in raw}
    return start, mapping


def get_subpairs(pair):
    a = pair[0] + MAPPING[pair]
    b = MAPPING[pair] + pair[1]
    return a, b


@memoize
def count_in_pair(letter, pair, expansions):
    if expansions == 0:
        value = pair.count(letter)
    else:
        sub_1, sub_2 = get_subpairs(pair)
        value = count_in_pair(letter, sub_1, expansions - 1) + count_in_pair(
            letter, sub_2, expansions - 1
        )

        correction = -1 if (sub_1[1] == sub_2[0] == letter) else 0
        value += correction
    return value


def count_in_word(letter, word, expansions):
    pairs = ["".join(x) for x in zip(word[:-1], word[1:])]
    value = sum(count_in_pair(letter, pair, expansions) for pair in pairs)

    correction = word[1:-1].count(letter)
    value -= correction
    return value


def solve(word, expansions):
    chars = set("".join(MAPPING.keys()))
    counts = {c: count_in_word(c, word, expansions) for c in chars}

    most_frequent = max(counts, key=counts.get)
    least_frequent = min(counts, key=counts.get)
    value = counts[most_frequent] - counts[least_frequent]
    return value


if __name__ == "__main__":
    word, MAPPING = get_cleaned_input()

    answer_1 = solve(word, 10)
    answer_2 = solve(word, 40)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
