from itertools import groupby
from utils import read, print_answers


def play(word, n):
    for _ in range(n):
        word = "".join(str(len(list(g))) + x for x, g in groupby(word))
    return len(word)


word = read(2015, 10)

a1 = play(word, 40)
a2 = play(word, 50)
print_answers(a1, a2, day=10)
