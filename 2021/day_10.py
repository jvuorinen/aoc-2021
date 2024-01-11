from utils import read_input

MATCH = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

ERROR_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

AUTOCOMPLETE_SCORE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def get_cleaned_input():
    inputs = read_input("inputs/day_10.txt")
    return inputs


def check_line(line):
    buffer = []
    for c in line:
        if c in "([{<":
            buffer.append(MATCH[c])
        elif c == buffer[-1]:
            buffer = buffer[:-1]
        else:
            return False, c
    ending = "".join(buffer[::-1])
    return True, ending


def check_all(inputs):
    endings = []
    error_chars = []
    for line in inputs:
        is_valid, value = check_line(line)
        if is_valid:
            endings.append(value)
        else:
            error_chars.append(value)
    return endings, error_chars


def count_ending_score(ending):
    score = 0
    for c in ending:
        score = 5 * score + AUTOCOMPLETE_SCORE[c]
    return score


if __name__ == "__main__":
    inputs = get_cleaned_input()

    endings, error_chars = check_all(inputs)
    scores = [count_ending_score(e) for e in endings]

    answer_1 = sum(ERROR_SCORE[c] for c in error_chars)
    answer_2 = sorted(scores)[len(scores) // 2]

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
