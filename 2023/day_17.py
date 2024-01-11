from heapq import heappush, heappop
from itertools import count
from utils import read_file, print_answers


def parse(raw_in):
    area = {complex(c, r): int(x) for r, row in enumerate(raw_in) for c, x in enumerate(row)}
    start = 0j
    end = list(area.keys())[-1]
    return area, start, end


def get_consecutive(path):
    c = 0
    d = path[-1] - path[-2]
    for i in range(1, len(path)):
        if path[-i] - path[-i - 1] == d:
            c += 1
        else:
            break
    return c


def get_next(path, area, use_ultra):
    if len(path) == 1:
        dirs = [1, -1, 1j, -1j]
    else:
        dirs = []
        fw = path[-1] - path[-2]
        cons = get_consecutive(path)
        if not use_ultra:
            dirs.append(fw * 1j)
            dirs.append(fw * -1j)
            if cons < 3:
                dirs.append(fw)
        else:
            if cons < 10:
                dirs.append(fw)
            if cons >= 4:
                dirs.append(fw * 1j)
                dirs.append(fw * -1j)
    return [path + [nxt] for d in dirs if (nxt := path[-1] + d) in area]


def dijsktra(area, start, end, use_ultra):
    id_gen = count(0)
    Q = []
    heappush(Q, (0, next(id_gen), [start]))
    seen = set()

    while Q:
        _d, _, _path = heappop(Q)
        for path in get_next(_path, area, use_ultra):
            loc = path[-1]
            d = _d + area[loc]
            if loc == end:
                return d
            cons = get_consecutive(path)
            hdg = path[-1] - path[-2]
            if (state := (loc, cons, hdg)) not in seen:
                seen.add(state)
                new = (d, next(id_gen), path)
                heappush(Q, new)


raw_in = read_file("inputs/day_17b.txt").split()
area, start, end = parse(raw_in)

a1 = dijsktra(area, start, end, use_ultra=False)
a2 = dijsktra(area, start, end, use_ultra=True)

print_answers(a1, a2, day=17)  # Correct: 902, 1073
