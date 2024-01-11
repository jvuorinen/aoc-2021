from utils import print_answers, read_file

raw_in = read_file("inputs/day_04.txt").split("\n")

a1 = 0
ns = [1 for _ in range(len(raw_in))]
for i, line in enumerate(raw_in):
    card = line.split(": ")[1].split(" | ")
    wins, own = [set(map(int, x.split())) for x in card]
    w = len(wins & own)
    a1 += 2 ** (w - 1) if w else 0
    for ii in range(w):
        ns[i + ii + 1] += ns[i]

print_answers(a1, sum(ns), day=4)  # Correct: 25004, 14427616
