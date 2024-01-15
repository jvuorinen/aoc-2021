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


def knot(word):
    inputs = [*map(ord, word)] + [17, 31, 73, 47, 23]
    lst = [x for x in range(256)]
    sparse = run(lst, inputs, 64)
    dense = [reduce(int.__xor__, sparse[i : i + 16]) for i in range(0, len(lst), 16)]
    return "".join(f"{x:02x}" for x in dense)


if __name__ == "__main__":
    raw = read(2017, 10)

    # Part 1
    inputs = [int(x) for x in raw.split(",")]
    lst = run([*range(256)], inputs, 1)
    a1 = lst[0] * lst[1]

    # Part 2
    a2 = knot(raw)

    print_answers(a1, a2, day=10)  # 212 96de9657665675b51cd03f0b3528ba26
