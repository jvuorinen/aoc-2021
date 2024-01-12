from itertools import combinations
from utils import read, print_answers

phrases = [x.split(" ") for x in read(2017, 4).split("\n")]


def not_anagram(words):
    return set(list(words[0])) != set(list(words[1]))


a1 = sum([len(p) == len(set(p)) for p in phrases])
a2 = sum([all(map(not_anagram, combinations(p, 2))) for p in phrases])

print_answers(a1, a2, day=4)  # 455 186
