from utils import read, print_answers


def parse(raw):
    replace = {
        "OR": "|",
        "AND": "&",
        "RSHIFT": ">>",
        "LSHIFT": "<<",
        "NOT": "~",
        "is": "_is",
        "as": "_as",
        "if": "_if",
        "in": "_in",
    }
    res = []
    for line in raw.split("\n"):
        for k, v in replace.items():
            line = line.replace(k, v)
        res.append(line.split(" -> "))
    return res


def run(prg):
    prg, mem = prg.copy(), {}
    while prg:
        cmd, tgt = prg.pop(0)
        try:
            exec(f"{tgt} = {cmd}", {}, mem)
        except NameError:
            prg.append((cmd, tgt))
    return mem["a"]


raw = read(2015, 7)
prg = parse(raw)

a1 = run(prg)

prg_mod = [(a1, t) if (t == "b") else (cmd, t) for cmd, t in prg]
a2 = run(prg_mod)

print_answers(a1, a2, day=7)
