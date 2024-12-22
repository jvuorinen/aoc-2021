from collections import defaultdict
from utils import read, print_answers

def run(program, a):
    mem = defaultdict(int)
    mem["a"] = a
    while mem["i"] < len(program):
        cmd, *args = program[mem["i"]].split(" ")
        # print(cmd, args, mem)
        match cmd:
            case "cpy":
                exec(f"{args[1]} = {args[0]}; i += 1", {}, mem)
            case "inc":
                exec(f"{args[0]} += 1; i += 1", {}, mem)
            case "dec":
                exec(f"{args[0]} -= 1; i += 1", {}, mem)
            case "jnz":
                exec(f"i += 1 if {args[0]} == 0 else {args[1]}",{},  mem)
            case "tgl":
                ti = mem["i"] + eval(args[0], {}, mem)
                # break
                if 0 <= ti < len(program):
                    tc, *targs = program[ti].split(" ")
                    if len(targs) == 1:
                        ct = "dec" if tc == "inc" else "inc"
                        program[ti] = f"{ct} {targs[0]}"
                    else:
                        ct = "cpy" if tc == "jnz" else "jnz"
                        program[ti] = f"{ct} {targs[0]} {targs[1]}"
                    # break
                mem["i"] += 1
    return mem["a"]

program = read().split("\n")
# program = read(2016, 23).split("\n")
# run(program, 7)


# a1 = run(program)
# a2 = run(program, part2=True)

# print_answers(a1, a2, day=23)  # 318020 9227674
