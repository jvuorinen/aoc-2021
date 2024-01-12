from collections import defaultdict
from utils import read, print_answers

cmds = read(2017, 8).split("\n")

best = 0
reg = defaultdict(int)
for cmd in cmds:
    instr, cond = cmd.split(" if ")
    a, b, c = cond.split(" ")
    if eval(f"reg['{a}'] {b} {c}"):
        d, e, f = instr.split(" ")
        op = ["-=", "+="][e == "inc"]
        exec(f"reg['{d}'] {op} {f}")
    best = max(best, max(reg.values()))

a1 = max(reg.values())

print_answers(a1, best, day=8)
