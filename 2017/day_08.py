from collections import defaultdict
from utils import read, print_answers

cmds = read(2017, 8).split("\n")

best = 0
reg = defaultdict(int)
for cmd in cmds:
    instr, cond = cmd.split(" if ")
    if eval(cond, {}, reg):
        instr = instr.replace('inc', "+=").replace('dec', "-=")
        exec(instr, {}, reg)
    best = max(best, max(reg.values()))

a1 = max(reg.values())

print_answers(a1, best, day=8)  # 4448 6582
