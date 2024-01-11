import numpy as np

from utils import print_answers, read_file

C = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
CI = {b: a for a, b in C.items()}


def snafu_to_dec(r):
    ds = [C[x] for x in list(r)][::-1]
    return sum([d * (5**i) for i, d in enumerate(ds)])


def dec_to_snafu(x):
    rev = list(map(int, np.base_repr(x, 5, padding=1)))[::-1]
    for p, _ in enumerate(rev):
        if rev[p] > 2:
            rev[p] -= 5
            rev[p + 1] += 1
    snf = (rev if rev[-1] != 0 else rev[:-1])[::-1]
    return "".join([CI[v] for v in snf])


if __name__ == "__main__":
    raw_in = read_file(f"inputs/day_25b.txt").split()
    s = sum([snafu_to_dec(x) for x in raw_in])

    a1 = dec_to_snafu(s)
    a2 = None

    print_answers(a1, a2, day=25)
    # 2-1=10=1=1==2-1=-221
