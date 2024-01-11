from utils import read, print_answers


def parse(fname):
    a, b = read(fname).split("\n\n")
    st = a.split(": ")[1]
    tmp = [tuple(line.split(" => ")) for line in b.split("\n")]
    notes = {a: b for a, b in tmp}
    return st, notes


def update(st, left_idx, notes):
    _st = f"....{st}...."
    res = "".join([notes.get(_st[i : i + 5], ".") for i in range(0, len(_st))])
    left_idx += res.index("#") - 2
    return res.strip("."), left_idx


def simulate(st):
    left_idx = 0
    history = [(st, left_idx)]
    while True:
        st, left_idx = update(st, left_idx, notes)
        history.append((st, left_idx))
        if history[-1][0] == history[-2][0]:
            return history


def score(history, generation):
    if generation <= len(history):
        st, left_idx = history[generation]
    else:
        delta = history[-1][1] - history[-2][1]
        st = history[-1][0]
        left_idx = history[-1][1] + delta * (generation - len(history) + 1)
    return sum([i for i, x in enumerate(st, left_idx) if x == "#"])


st, notes = parse("inputs/day_12b.txt")
history = simulate(st)

a1 = score(history, 20)
a2 = score(history, 50000000000)
print_answers(a1, a2, day=12)
