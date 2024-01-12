from utils import read, print_answers

raw = read(2017, 5).split("\n")
mem = [*map(int, raw)]


def run(mem, part1=True):
    mem = mem.copy()
    c = i = 0
    while c < len(mem):
        offset = 1 if part1 or mem[c] < 3 else -1
        mem[c] += offset
        c += mem[c] - offset
        i += 1
    return i


a1 = run(mem)
a2 = run(mem, False)

print_answers(a1, a2, day=99)  # 394829 31150702
