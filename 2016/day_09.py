from functools import cache
import re
from utils import read, print_answers

s = read(2016, 9)


def cut(data):
    first, *rest = re.split(r"(\([^)]+\))", data, maxsplit=1)
    if first:
        return first, "".join(rest)
    a, b = map(int, rest[0][1:-1].split("x"))
    return rest[1][:a] * b, rest[1][a:]


@cache
def get_size(data, simple=True):
    if simple or "(" not in data:
        return len(data)
    first, rest = cut(data)
    return get_size(first, simple) + get_size(rest, simple)


a1 = get_size(s)
a2 = get_size(s, False)

print_answers(a1, a2, day=9)  # 152851 11797310782
