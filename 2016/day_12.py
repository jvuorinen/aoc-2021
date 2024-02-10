from collections import defaultdict
from utils import read, print_answers

cmds = read(2016, 12).split("\n")


def run(cmds, part2=False):
    mem = defaultdict(int)
    if part2:
        mem["c"] = 1
    while mem["i"] < len(cmds):
        cmd = cmds[mem["i"]]
        if mem["i"] == 10:
            mem["a"] += mem["b"] - 1
            mem["b"] -= mem["b"] - 1
        match cmd.split(" "):
            case "cpy", x1, x2:
                exec(f"{x2} = {x1}", {}, mem)
                mem["i"] += 1
            case "inc", x1:
                exec(f"{x1} += 1", {}, mem)
                mem["i"] += 1
            case "dec", x1:
                exec(f"{x1} -= 1", {}, mem)
                mem["i"] += 1
            case "jnz", x1, x2:
                exec(f"i += 1 if {x1} == 0 else ({x2})", {}, mem)
    return mem["a"]


a1 = run(cmds)
a2 = run(cmds, part2=True)

print_answers(a1, a2, day=12)
