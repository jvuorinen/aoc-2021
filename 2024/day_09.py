from utils import read, print_answers


def solve1(data):
    data = data.copy()
    i, ii = 0, len(data) - 1
    while True:
        while data[i] is not None:
            i += 1
        while data[ii] is None:
            ii -= 1
        if ii <= i:
            return sum(i * (x or 0) for i, x in enumerate(data))
        data[i], data[ii] = data[ii], data[i]


def solve2(data):
    data = data.copy()

    file_ixs = [data.index(i) for i in range(len(files))]
    empty_areas = []
    for fi, fii, f in zip(file_ixs, file_ixs[1:], files):
        empty_idx = fi + len(f)
        empty_size = fii - (fi + len(f))
        if empty_size:
            empty_areas.append((empty_idx, empty_size))

    for ii, f in zip(file_ixs[::-1], files[::-1]):
        s = len(f)
        for j, (i, es) in enumerate(empty_areas):
            if i >= ii:
                break
            if es < s:
                continue
            data[i : i + s] = f
            data[ii : ii + s] = [None] * s
            empty_areas.pop(j)
            if ns := es - s:
                empty_areas.insert(j, (i + s, ns))
            break

    return sum(i * (x or 0) for i, x in enumerate(data))


raw = read(2024, 9)

files = [int(c) * [i] for i, c in enumerate(raw[::2])]
empty = [int(c) * [None] for c in raw[1::2]]

data = []
for f, e in zip(files, empty + [[None]]):
    data.extend(f)
    data.extend(e)

a1 = solve1(data)
a2 = solve2(data)

print_answers(a1, a2, day=9)
