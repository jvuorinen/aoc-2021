from functools import reduce
from utils import read, print_answers


def run(lst, inputs, times):
    lst = lst.copy()
    s = 0
    for sk, ip in enumerate(inputs * times):
        lst = lst[:ip][::-1] + lst[ip:]
        p = (ip + sk) % len(lst)
        s += p
        lst = lst[p:] + lst[:p]
    st = -s % len(lst)
    lst = lst[st:] + lst[:st]
    return lst


raw = read(2017, 10)
lst = [x for x in range(256)]

# Part 1
inputs = [int(x) for x in raw.split(",")]
_lst = run(lst, inputs, 1)
a1 = _lst[0] * _lst[1]

# Part 2
inputs = [*map(ord, raw)] + [17, 31, 73, 47, 23]
sparse = run(lst, inputs, 64)
dense = [reduce(int.__xor__, sparse[i : i + 16]) for i in range(0, len(sparse), 16)]
a2 = "".join([hex(x)[2:].zfill(2) for x in dense])

print_answers(a1, a2, day=9)  # 212 96de9657665675b51cd03f0b3528ba26
