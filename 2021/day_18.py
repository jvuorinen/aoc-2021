import re
from functools import reduce
from itertools import permutations

from utils import read_input


def parse_sfn(str_sfn):
    numbers = []
    depth = 0
    for x in str_sfn:
        if x == "[":
            depth += 1
        elif x == "]":
            depth -= 1
        elif re.match(r"\d", x):
            numbers.append((int(x), depth))
    return numbers


def get_cleaned_input():
    raw_in = read_input("inputs/day_18.txt")
    sfn_list = [parse_sfn(str_sfn) for str_sfn in raw_in]
    return sfn_list


def explode_first(sfn):
    cp = sfn[:]
    for i, (n, depth) in enumerate(cp):
        if depth > 4:
            if i > 0:
                exp_a = n
                prev_n, prev_d = cp[i - 1]
                cp[i - 1] = (prev_n + exp_a, prev_d)
            if i < len(cp) - 2:
                exp_b = cp[i + 1][0]
                next_n, next_d = cp[i + 2]
                cp[i + 2] = (next_n + exp_b, next_d)
            cp[i] = (0, depth - 1)
            cp.pop(i + 1)
            return cp, True
    return cp, False


def split_first(sfn):
    cp = sfn[:]
    for i, (n, depth) in enumerate(cp):
        if n > 9:
            cp.pop(i)
            cp.insert(i, ((n // 2) + (n % 2), depth + 1))
            cp.insert(i, (n // 2, depth + 1))
            return cp, True
    return cp, False


def reduce_sfn(sfn):
    cp = sfn[:]
    while True:
        cp, has_exploded = explode_first(cp)
        if has_exploded:
            continue
        cp, has_split = split_first(cp)
        if (not has_exploded) and (not has_split):
            return cp


def add_sfn(sfn_a, sfn_b):
    inc_a = [(n, d + 1) for n, d in sfn_a]
    inc_b = [(n, d + 1) for n, d in sfn_b]
    sfn = inc_a + inc_b

    result = reduce_sfn(sfn)
    return result


def listify(sfn, max_depth=None):
    if not max_depth:
        max_depth = max(x[1] for x in sfn)

    if max_depth == 1:
        a = sfn[0][0]
        b = sfn[1][0]
        return [a, b]
    else:
        cp = sfn[:]
        i = 0
        while True:
            p, d = cp[i]
            np, nd = cp[i + 1]
            if d == nd == max_depth:
                del cp[i]
                del cp[i]
                cp.insert(i, ([p, np], d - 1))
            i += 1
            if i >= len(cp) - 1:
                break

        return listify(cp, max_depth - 1)


def _get_magnitude(sfn_list):
    a, b = sfn_list[0], sfn_list[1]
    a = a if (type(a) == int) else _get_magnitude(a)
    b = b if (type(b) == int) else _get_magnitude(b)
    s = 3 * a + 2 * b
    return s


def get_magnitude(sfn):
    as_list = listify(sfn)
    m = _get_magnitude(as_list)
    return m


def solve_1(sfn_list):
    sfn_sum = reduce(add_sfn, sfn_list)
    m = get_magnitude(sfn_sum)
    return m


def solve_2(sfn_list):
    def magnitude_of_sum(a, b):
        return get_magnitude(add_sfn(a, b))

    best = max(magnitude_of_sum(a, b) for a, b in permutations(sfn_list, 2))
    return best


if __name__ == "__main__":
    sfn_list = get_cleaned_input()

    answer_1 = solve_1(sfn_list)
    answer_2 = solve_2(sfn_list)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
