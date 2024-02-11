from functools import cache
from hashlib import md5
from utils import print_answers, read

SALT = read(2016, 14)


@cache
def streched_hash(n, streches):
    s = SALT + str(n)
    for _ in range(streches + 1):
        s = md5(s.encode()).hexdigest()
    return s


@cache
def get_consecutives(n, length, streches):
    hsh = streched_hash(n, streches)
    res = []
    for z in zip(*[hsh[i:] for i in range(length)]):
        if len(set(z)) == 1:
            res.append(z[0])
    return res


def is_key(n, streches):
    trp = get_consecutives(n, 3, streches)
    return trp and any(trp[0] in get_consecutives(n + i, 5, streches) for i in range(1, 1001))


def get_final_key(streches):
    keys, i = [], 1
    for i in range(1000000):
        if is_key(i, streches):
            keys.append(i)
            if len(keys) == 64:
                return keys[-1]


a1 = get_final_key(0)
a2 = get_final_key(2016)

print_answers(a1, a2, day=14)  # 23890 22696
