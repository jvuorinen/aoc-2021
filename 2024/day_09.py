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


def solve2(data, idx_file, idx_empty, empty):
    data = data.copy()
    empty_areas = [(ie, len(e)) for ie, e in zip(idx_empty, empty) if e]

    for ii, f in zip(idx_file[::-1], files[::-1]):
        s = len(f)
        for ie, (i, es) in enumerate(empty_areas):
            if i >= ii:
                break
            if es < s:
                continue
            data[i : i + s] = f
            data[ii : ii + s] = [None] * s
            empty_areas.pop(ie)
            if ns := es - s:
                empty_areas.insert(ie, (i + s, ns))
            break

    return sum(i * (x or 0) for i, x in enumerate(data))


raw = read(2024, 9)

files = [int(c) * [i] for i, c in enumerate(raw[::2])]
empty = [int(c) * [None] for c in raw[1::2]]

i = 0
data, idx_file, idx_empty = [], [], []
for f, e in zip(files, empty + [[None]]):
    data.extend(f)
    data.extend(e)
    idx_file.append(i)
    idx_empty.append(i := i + len(f))
    i += len(e)

a1 = solve1(data)
a2 = solve2(data, idx_file, idx_empty, empty)

print_answers(a1, a2, day=9)
