from collections import defaultdict
from utils import read, print_answers


cmds = read(2017, 23).split("\n")

mem = defaultdict(int)
i = 0
a1 = 0
while i < len(cmds):
    op, *args = cmds[i].split()
    i += 1
    match op:
        case "set":
            exec(f"{args[0]} = {args[1]}", {}, mem)
        case "sub":
            exec(f"{args[0]} -= {args[1]}", {}, mem)
        case "mul":
            a1 += 1
            exec(f"{args[0]} *= {args[1]}", {}, mem)
        case "jnz":
            if eval(f"{args[0]} != 0", {}, mem):
                i += int(eval(f"{args[1]}", {}, mem) - 1)


def not_prime(n):
    return any(n % i == 0 for i in range(2, int(n**0.5) + 1))


a2 = sum([not_prime(x) for x in range(109900, 109900 + 17001, 17)])

print_answers(a1, a2, day=23)  # 9409 913
