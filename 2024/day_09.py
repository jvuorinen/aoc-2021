from utils import read, print_answers


def checksum(data):
    return sum(i * (x or 0) for i, x in enumerate(data))


def unfold(blocks):
    nested = [[i // 2 if i % 2 == 0 else None] * b[1] for i, b in enumerate(blocks)]
    return [x for xs in nested for x in xs]


def solve1(blocks):
    data = unfold(blocks)
    i, ii = 0, len(data) - 1
    while True:
        while data[i] is not None:
            i += 1
        while data[ii] is None:
            ii -= 1
        if ii <= i:
            return checksum(data)
        data[i], data[ii] = data[ii], data[i]


def solve2(blocks):
    data = unfold(blocks)
    files = [*enumerate(blocks[::2])]
    empty = [b for b in blocks[1::2] if b[1]]
    for f_id, (ii, sf) in files[::-1]:
        for ie, (i, se) in enumerate(empty):
            if i >= ii:
                break
            if se >= sf:
                data[i : i + sf] = [f_id] * sf
                data[ii : ii + sf] = [None] * sf
                empty.pop(ie)
                if ns := se - sf:
                    empty.insert(ie, (i + sf, ns))
                break
    return checksum(data)


raw = read(2024, 9)
i = 0
ixs = [i := i + int(x) for x in list('0' + raw)]
blocks = [(i, int(x)) for i, x in zip(ixs, list(raw))]

a1 = solve1(blocks)
a2 = solve2(blocks)

print_answers(a1, a2, day=9)
