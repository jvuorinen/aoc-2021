from itertools import product
from tqdm import tqdm
from utils import read, print_answers

# raw = read().split("\n")
raw = read(2024, 7).split("\n")

a1 = 0
tot = set()

for line in tqdm(raw):
    a, b = line.split(': ')
    a = int(a)
    b = b.split(' ')

    size = len(b) - 1

    for ops in product(*[list('+*') for _ in range(size)]):
        ints = [int(x) for x in b]
        res = ints.pop(0)
        for op in ops:
            if op == '|':
                res = int(f"{res}{ints.pop(0)}")
            else:
                exec(f'res = res {op} {ints.pop(0)}')
        if res == a:
            tot.add(a)
            break


a1 = sum(tot)
a2 = None

print_answers(a1, a2, day=7)
# 3351424677624
# 204976636995111