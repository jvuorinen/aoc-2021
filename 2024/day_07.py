from itertools import product
from tqdm import tqdm
from utils import read, print_answers


def check(line, ops):
    a, b = line.split(': ')
    a = int(a)
    b = b.split(' ')
    size = len(b) - 1

    for oc in product(*[list(ops) for _ in range(size)]):
        ints = [int(x) for x in b]
        res = ints.pop(0)
        for op in oc:
            x = ints.pop(0)
            if op == '|':
                res = int(f"{res}{x}")
            else:
                res = eval(f'res {op} {x}')
        if res == a:
            return a
    return 0


# lines = read().split("\n")
lines = read(2024, 7).split("\n")

a1 = sum(set(check(line, '+*') for line in tqdm(lines)))
a2 = sum(set(check(line, '+*') or check(line, '+*|') for line in tqdm(lines)))

print_answers(a1, a2, day=7)
# 3351424677624
# 204976636995111