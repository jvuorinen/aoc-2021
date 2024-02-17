from utils import read, print_answers


def do(data, size):
    while len(data) < size:
        data = data + "0" + "".join("1" if x == "0" else "0" for x in data[::-1])
    data = data[:size]
    while len(data) % 2 == 0:
        data = "".join("1" if a == b else "0" for a, b in zip(data[0::2], data[1::2]))
    return data


data = read(2016, 16)

a1 = do(data, 272)
a2 = do(data, 35651584)

print_answers(a1, a2, day=99)
