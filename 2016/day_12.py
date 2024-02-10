from collections import defaultdict
from utils import read, print_answers


def parse(raw):
    program = []
    for line in raw:
        cmd, *args = line.split(" ")
        match cmd:
            case "cpy":
                program.append(f"{args[1]} = {args[0]}; i += 1")
            case "inc":
                program.append(f"{args[0]} += 1; i += 1")
            case "dec":
                program.append(f"{args[0]} -= 1; i += 1")
            case "jnz":
                program.append(f"i += 1 if {args[0]} == 0 else {args[1]}")
    return program


def run(program, part2=False):
    mem = defaultdict(int)
    if part2:
        mem["c"] = 1
    while mem["i"] < len(program):
        cmd = program[mem["i"]]
        if mem["i"] == 10:
            shortcut = mem["b"] - 1
            mem["a"] += shortcut
            mem["b"] -= shortcut
        exec(cmd, {}, mem)
    return mem["a"]


raw = read(2016, 12).split("\n")
program = parse(raw)

a1 = run(program)
a2 = run(program, part2=True)

print_answers(a1, a2, day=12)  # 318020 9227674
