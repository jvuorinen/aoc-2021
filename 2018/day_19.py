from utils import read, print_answers


def do(r, to, res):
    _r = r[:]
    _r[to] = res
    return _r


ops = {
    "addr": lambda r, i: do(r, i[3], r[i[1]] + r[i[2]]),
    "addi": lambda r, i: do(r, i[3], r[i[1]] + i[2]),
    "mulr": lambda r, i: do(r, i[3], r[i[1]] * r[i[2]]),
    "muli": lambda r, i: do(r, i[3], r[i[1]] * i[2]),
    "banr": lambda r, i: do(r, i[3], r[i[1]] & r[i[2]]),
    "bani": lambda r, i: do(r, i[3], r[i[1]] & i[2]),
    "borr": lambda r, i: do(r, i[3], r[i[1]] | r[i[2]]),
    "bori": lambda r, i: do(r, i[3], r[i[1]] | i[2]),
    "setr": lambda r, i: do(r, i[3], r[i[1]]),
    "seti": lambda r, i: do(r, i[3], i[1]),
    "gtir": lambda r, i: do(r, i[3], int(i[1] > r[i[2]])),
    "gtri": lambda r, i: do(r, i[3], int(r[i[1]] > i[2])),
    "gtrr": lambda r, i: do(r, i[3], int(r[i[1]] > r[i[2]])),
    "eqir": lambda r, i: do(r, i[3], int(i[1] == r[i[2]])),
    "eqri": lambda r, i: do(r, i[3], int(r[i[1]] == i[2])),
    "eqrr": lambda r, i: do(r, i[3], int(r[i[1]] == r[i[2]])),
}


raw = read("inputs/day_19b.txt").split("\n")
ip = int(raw[0].split()[1])
code = []
for line in raw[1:]:
    op, *args = line.split()
    code.append((op, int(args[0]), int(args[1]), int(args[2])))

reg = [0, 0, 0, 0, 0, 0]
while reg[ip] < len(code):
    i = reg[ip]
    ins = code[i]
    # print(f"Reg {reg}".ljust(30) + f"Ins {i}: {' '.join(map(str, ins))}")
    reg = ops[ins[0]](reg, ins)
    reg[ip] += 1

a1 = reg[0]

D = 10551331
a2 = sum([i for i in range(1, D + 1) if (D % i == 0)])

print_answers(a1, a2, day=19)  # 1140, 12474720
