from itertools import permutations
from collections import Counter

from utils import read_input


SEGMENT_TO_DIGIT = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def parse_line(line):
    a, b = line.split(" | ")
    t = (a.split(), b.split())
    return t


def get_cleaned_input():
    raw_in = read_input("inputs/day_08.txt")
    in_letters, out_letters = zip(*[parse_line(l) for l in raw_in])
    return in_letters, out_letters


def rewire(segments, wiring):
    result = set(wiring[x] for x in segments)
    s = "".join(sorted(result))
    return s


def validate_wiring(inputs, outputs, wiring):
    for segments in inputs + outputs:
        rewired = rewire(segments, wiring)
        if rewired not in SEGMENT_TO_DIGIT:
            return False
    return True


def find_wiring(inputs, outputs):
    possible_wirings = [{a: b for a, b in zip(p, "abcdefg")} for p in permutations("abcdefg")]

    for wiring in possible_wirings:
        valid = validate_wiring(inputs, outputs, wiring)
        if valid:
            return wiring


def decode_number(outputs, wiring):
    s = "".join(SEGMENT_TO_DIGIT[rewire(n, wiring)] for n in outputs)
    out_number = int(s)
    return out_number


def get_output_numbers(all_inputs, all_outputs):
    out = []
    for inputs, outputs in zip(all_inputs, all_outputs):
        wiring = find_wiring(inputs, outputs)
        out_number = decode_number(outputs, wiring)
        out.append(out_number)

    return out


def count_1478(out_numbers):
    as_str = "".join(map(str, out_numbers))
    c = Counter(as_str)
    s = c["1"] + c["4"] + c["7"] + c["8"]
    return s


if __name__ == "__main__":
    all_inputs, all_outputs = get_cleaned_input()
    out_numbers = get_output_numbers(all_inputs, all_outputs)

    answer_1 = count_1478(out_numbers)
    answer_2 = sum(out_numbers)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
