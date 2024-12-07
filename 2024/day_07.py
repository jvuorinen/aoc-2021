from itertools import product
from tqdm import tqdm
from utils import read, print_answers


def check(line, ops):
    _exp, _ns = line.split(': ')
    exp = int(_exp)
    ns = [int(x) for x in _ns.split(' ')]

    for cmb in product(*[list(ops) for _ in range(len(ns) - 1)]):
        # print(cmb)
        ints = ns.copy()
        res = ints.pop(0)
        for op in cmb:
            x = ints.pop(0)
            if op == '|':
                res = int(f"{res}{x}")
            else:
                res = eval(f'res {op} {x}')
        if res == exp:
            # print("OO")
            return exp
    return 0


lines = read().split("\n")
# lines = read(2024, 7).split("\n")

a1 = sum(check(x, '*+') for x in tqdm(lines))
a2 = sum(check(x, '*+') or check(x, '*|+') for x in tqdm(lines))

print_answers(a1, a2, day=7)
# 3351424677624
# 204976636995111