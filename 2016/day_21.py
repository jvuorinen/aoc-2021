from itertools import permutations
from functools import reduce
from re import findall
from utils import read, print_answers


def _step(lst, line):
    lst = lst.copy()
    if "swap position" in line:
        a, b = map(int, findall(r"\d", line))
        lst[a], lst[b] = lst[b], lst[a]
    elif "swap letter" in line:
        a, b = findall(r"letter (.)", line)
        ia, ib = lst.index(a), lst.index(b)
        lst[ia], lst[ib] = lst[ib], lst[ia]
    elif "reverse" in line:
        a, b = map(int, findall(r"\d", line))
        lst[a:b+1] = lst[a:b+1][::-1]
    elif "move" in line:
        a, b = map(int, findall(r"\d", line))
        lst.insert(b, lst.pop(a))
    elif "rotate" in line:
        if "based" in line:
            a = findall(r"letter (.)", line)[0]
            ia = lst.index(a)
            n = -(1 + ia + (ia >= 4))
        else:
            n = int(findall(r"(.) step", line)[0])
            if "right" in line:
                n *= -1
        n %= len(lst)
        lst = lst[n:] + lst[:n]
    return lst


def fumble(text):
    return "".join(reduce(_step, lines, list(text)))


lines = read(2016, 21).split("\n")

a1 = fumble('abcdefgh')
a2 = next("".join(p) for p in permutations('abcdefgh') if (fmb := fumble(p)) == 'fbgdceah')

print_answers(a1, a2, day=21)
