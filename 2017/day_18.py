from collections import defaultdict
from utils import read, print_answers

cmds = read(2017, 18).split("\n")


def run(p, cmds, out):
    mem = defaultdict(int)
    mem["p"] = p
    i = 0
    while True:
        op, *args = cmds[i].split()
        i += 1
        match op:
            case "set":
                exec(f"{args[0]} = {args[1]}", {}, mem)
            case "add":
                exec(f"{args[0]} += {args[1]}", {}, mem)
            case "mul":
                exec(f"{args[0]} *= {args[1]}", {}, mem)
            case "mod":
                exec(f"{args[0]} %= {args[1]}", {}, mem)
            case "jgz":
                if eval(f"{args[0]} > 0", {}, mem):
                    i += int(eval(f"{args[1]}", {}, mem) - 1)
            case "snd":
                out.append((p, mem[args[0]]))
            case "rcv":
                mem[args[0]] = yield


queue = []
progs = [run(0, cmds, queue), run(1, cmds, queue)]
next(progs[0])
next(progs[1])

a1 = [msg for snd, msg in queue if snd == 0][-1]

a2 = 0
while queue:
    sender, val = queue.pop(0)
    if sender == 1:
        a2 += 1
    progs[sender ^ 1].send(val)

print_answers(a1, a2, day=18)  # 2951 7366
