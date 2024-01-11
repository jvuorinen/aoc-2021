from itertools import combinations

from utils import chunked, read_input


def find_invalid_number(inputs, preamble_length):
    for i in range(preamble_length, len(inputs) - 1):
        preamble = inputs[(i - preamble_length) : i]
        test_value = inputs[i]

        if test_value not in set((a + b) for a, b in combinations(preamble, 2)):
            return test_value


def find_weakness(inputs, invalid_number):
    for chunk_length in range(2, len(inputs)):
        chunks = chunked(inputs, chunk_length, no_overlap=False)
        for c in chunks:
            as_list = list(c)
            if sum(as_list) == invalid_number:
                return min(as_list) + max(as_list)


if __name__ == "__main__":
    numbers = [int(x) for x in read_input("inputs/day_09.txt")]

    invalid_number = find_invalid_number(numbers, 25)
    weakness = find_weakness(numbers, invalid_number)

    print(f"Part 1 answer: {invalid_number}")
    print(f"Part 2 answer: {weakness}")
