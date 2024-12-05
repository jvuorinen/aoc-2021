from utils import read, print_answers

raw = read(2016, 20).split("\n")
blocks = [tuple(int(x) for x in b.split("-")) for b in raw]

valids = [(0, 4294967295)]
for b in blocks:
    _valids = []
    for v in valids:
        if (v[1] < b[0]) or (b[1] < v[0]):
            _valids += [v]
        else:
            if v[0] < b[0]:
                _valids += [(v[0], b[0] - 1)]
            if b[1] < v[1]:
                _valids += [(b[1] + 1, v[1])]
    valids = _valids

a1 = min(v[0] for v in valids)
a2 = sum(v[1] - v[0] + 1 for v in valids)

print_answers(a1, a2, day=20)
