from re import findall
from utils import read


def get_line(cmd, arg):
    CMB = [0, 1, 2, 3, "a", "b", "c"]
    return {
        0: f"a = a // 2 ** {CMB[arg % 7]}",
        1: f"b = b ^ {arg}",
        2: f"b = {CMB[arg % 7]} % 8",
        3: f"# jnz {arg}",
        4: "b = b ^ c",
        5: f"out.append({CMB[arg % 7]} % 8)",
        6: f"b = a // 2 ** {CMB[arg % 7]}",
        7: f"c = a // 2 ** {CMB[arg % 7]}",
    }[cmd]


def disassemble(prg, mem):
    init = "def run():\n"
    init += "".join(f"    {k} = {v}\n" for k, v in mem.items())
    init += "    out = []\n\n"
    return (
        init
        + "\n".join(
            "    " + get_line(c, a) + f"  #{i}" for i, (c, a) in enumerate(zip(prg[::2], prg[1::2]))
        )
        + "\n    return out"
    )


p1, p2 = read(2024, 17).split("\n\n")
a, b, c = map(int, findall(r"\d+", p1))
mem = {"a": a, "b": b, "c": c}
prg = [*map(int, p2.split(" ")[1].split(","))]

python = disassemble(prg, mem)
print(python)
