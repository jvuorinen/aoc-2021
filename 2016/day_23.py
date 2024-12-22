from collections import defaultdict
from utils import read, print_answers


def run(program, a):
    program = program.copy()
    mem = defaultdict(int)
    mem["a"] = a
    j = 0
    tgl = 0
    while j < 100000 and mem["i"] < len(program):
        j += 1
        cmd, *args = program[mem["i"]].split(" ")
        match cmd:
            case "cpy":
                exec(f"{args[1]} = {args[0]}; i += 1", {}, mem)
            case "inc":
                exec(f"{args[0]} += 1; i += 1", {}, mem)
            case "dec":
                exec(f"{args[0]} -= 1; i += 1", {}, mem)
            case "jnz":
                # hack
                if mem["i"] == 7:
                    mem["a"] += mem["c"]
                    mem["c"] = 0
                if mem["i"] == 9:
                    mem["a"] += mem["a"] * mem["d"]
                    mem["d"] = 0
                # /hack
                exec(f"i += 1 if {args[0]} == 0 else {args[1]}", {}, mem)
            case "tgl":
                ti = mem["i"] + eval(args[0], {}, mem)
                if 0 <= ti < len(program):
                    tgl += 1
                    tc, *targs = program[ti].split(" ")
                    if len(targs) == 1:
                        ct = "dec" if tc == "inc" else "inc"
                        program[ti] = f"{ct} {targs[0]}"
                    else:
                        ct = "cpy" if tc == "jnz" else "jnz"
                        program[ti] = f"{ct} {targs[0]} {targs[1]}"
                mem["i"] += 1
    return mem["a"]


program = read(2016, 23).split("\n")

a1 = run(program, 7)
a2 = run(program, 12)

print_answers(a1, a2, day=23)
