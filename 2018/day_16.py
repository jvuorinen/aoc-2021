import re
import numpy as np
from scipy.optimize import linear_sum_assignment
from utils import read, print_answers


def parse(raw):
    s, i = raw.split("\n\n\n\n")
    pat = r"(\d+)[, ]+(\d+)[, ]+(\d+)[, ]+(\d+)"
    samples = [[tuple(map(int, x)) for x in re.findall(pat, _s)] for _s in s.split("\n\n")]
    code = [tuple(map(int, x)) for x in re.findall(pat, i)]
    return samples, code


def do(r, to, res):
    _r = list(r)
    _r[to] = res
    return tuple(_r)


ops = [
    lambda r, i: do(r, i[3], r[i[1]] + r[i[2]]),  # addr
    lambda r, i: do(r, i[3], r[i[1]] + i[2]),  # addi
    lambda r, i: do(r, i[3], r[i[1]] * r[i[2]]),  # mulr
    lambda r, i: do(r, i[3], r[i[1]] * i[2]),  # muli
    lambda r, i: do(r, i[3], r[i[1]] & r[i[2]]),  # banr
    lambda r, i: do(r, i[3], r[i[1]] & i[2]),  # bani
    lambda r, i: do(r, i[3], r[i[1]] | r[i[2]]),  # borr
    lambda r, i: do(r, i[3], r[i[1]] | i[2]),  # bori
    lambda r, i: do(r, i[3], r[i[1]]),  # setr
    lambda r, i: do(r, i[3], i[1]),  # seti
    lambda r, i: do(r, i[3], int(i[1] > r[i[2]])),  # gtir
    lambda r, i: do(r, i[3], int(r[i[1]] > i[2])),  # gtri
    lambda r, i: do(r, i[3], int(r[i[1]] > r[i[2]])),  # gtrr
    lambda r, i: do(r, i[3], int(i[1] == r[i[2]])),  # eqir
    lambda r, i: do(r, i[3], int(r[i[1]] == i[2])),  # eqri
    lambda r, i: do(r, i[3], int(r[i[1]] == r[i[2]])),  # eqrr
]


raw = read("inputs/day_16b.txt")
samples, code = parse(raw)

# Determine opcode pairing
n_possible = []
possible = np.array([[True] * len(ops)] * len(ops))
for bf, i, af in samples:
    sample_possible = [(op(bf, i) == af) for op in ops]
    n_possible.append(sum(sample_possible))
    possible[i[0]] &= sample_possible

_, pairing = linear_sum_assignment(possible, maximize=True)

# Run code
reg = (0, 0, 0, 0)
for i in code:
    op = ops[pairing[i[0]]]
    reg = op(reg, i)

a1 = sum([x >= 3 for x in n_possible])
a2 = reg[0]
print_answers(a1, a2, day=16)  # 3674, 533
