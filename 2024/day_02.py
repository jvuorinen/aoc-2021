import numpy as np
from utils import read, print_answers


def is_safe(rep):
    d = np.diff(rep)
    return (all(d < 0) or all(d > 0)) and all(abs(d) >= 1) and all(abs(d) <= 3)


def is_safe_pro(rep):
    subreps = (np.delete(rep, i) for i in range(len(rep)))
    return is_safe(rep) or any(is_safe(r) for r in subreps)


raw = read(2024, 2)
reports = [np.array(x.split()).astype(int) for x in raw.split("\n")]

a1 = sum(is_safe(r) for r in reports)
a2 = sum(is_safe_pro(r) for r in reports)

print_answers(a1, a2, day=2)
