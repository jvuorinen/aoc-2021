from utils import read, print_answers


def get_possible(pieces, bridge):
    results = []
    for p in pieces:
        if bridge[-1] in p:
            flipped = p if p[0] == bridge[-1] else p[::-1]
            results.append((pieces - {p}, tuple([*bridge] + [*flipped])))
    return results


def get_best(pieces, bridge, f):
    if nxt := get_possible(pieces, bridge):
        return max([get_best(p, b, f) for p, b in nxt])
    return f(bridge)


raw = read(2017, 24).split("\n")
pieces = set([tuple(map(int, x.split("/"))) for x in raw])

a1 = get_best(pieces, tuple([0]), sum)
a2 = get_best(pieces, tuple([0]), lambda x: (len(x), sum(x)))[1]

print_answers(a1, a2, day=24)  # 1868 1841
