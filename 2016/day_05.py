from hashlib import md5
from utils import read, print_answers

base = read(2016, 5)

def solve(base):
    pw1 = []
    pw2 = [None for _ in range(8)]
    i = 0
    while None in pw2:
        hx = md5(f"{base}{i}".encode()).hexdigest()
        if hx[:5] == "00000":
            sixth = hx[5]
            pw1.append(sixth)
            if (loc := int(sixth, 16)) < 8 and pw2[loc] is None:
                pw2[loc] = hx[6]
        i += 1
    return map("".join, (pw1[:8], pw2))

a1, a2 = solve(base)
print_answers(a1, a2, day=5)  # 2414bc77 437e60fc
