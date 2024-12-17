from re import findall
from utils import read, print_answers

p1, p2 = read(2024, 17).split("\n\n")
a, b, c = map(int, findall(r"\d+", p1))
mem = {"a": a, "b": b, "c": c}
prg = [*map(int, p2.split(" ")[1].split(","))]


def get_combo(i, mem):
    return [0, 1, 2, 3, mem["a"], mem["b"], mem["c"]][i]


def run(prg, mem):
    mem = mem.copy()
    i = 0
    res = []
    while i < len(prg):
        cmd = prg[i]
        if cmd == 0:
            mem["a"] = mem["a"] // 2 ** get_combo(prg[i + 1], mem)
        elif cmd == 1:
            mem["b"] = mem["b"] ^ prg[i + 1]
        elif cmd == 2:
            mem["b"] = get_combo(prg[i + 1], mem) % 8
        elif cmd == 4:
            mem["b"] = mem["b"] ^ mem["c"]
        elif cmd == 5:
            val = get_combo(prg[i + 1], mem) % 8
            res.append(val)
        elif cmd == 6:
            mem["b"] = mem["a"] // 2 ** get_combo(prg[i + 1], mem)
        elif cmd == 7:
            mem["c"] = mem["a"] // 2 ** get_combo(prg[i + 1], mem)

        if cmd == 3 and mem["a"] != 0 and (j := prg[i + 1]) != i:
            i = j
        else:
            i += 2
    return res


def to_int(b8):
    return int("".join(map(str, b8)), 8)


def find_magic_number(b8=None, ix=0):
    if ix == len(prg):
        return to_int(b8)
        
    for i in range(8):
        b8[ix] = i
        tst = run(prg, mem | {"a": to_int(b8)})
        if tst[-(ix + 1) :] == prg[-(ix + 1) :]:
            if res := find_magic_number(b8.copy(), ix + 1):
                return res


a1 = ",".join(map(str, run(prg, mem)))
a2 = find_magic_number([0 for _ in range(16)])

print_answers(a1, a2, day=17)
