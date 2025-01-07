from itertools import groupby
from utils import read, print_answers
from string import ascii_lowercase

CHARS = sorted(set(ascii_lowercase))


# br = base representation
def check(br):
    if (1, 2) not in ((a - b, a - c) for a, b, c in zip(br[:-2], br[1:-1], br[2:])):
        return False
    if len({n for n, g in groupby(br) if len(list(g)) >= 2}) <= 1:
        return False
    return True


def increment(br):
    for i in range(len(br)):
        br[i] += 2 if CHARS[(br[i] + 1) % len(CHARS)] in "iol" else 1
        if br[i] < len(CHARS):
            return
        br[i] = 0


def rotator(pw):
    br = [ord(x) - ord("a") for x in pw[::-1]]
    while True:
        if check(br):
            yield "".join(CHARS[x] for x in br)[::-1]
        increment(br)


pw = read(2015, 11)
gen = rotator(pw)

print_answers(next(gen), next(gen), day=11)
