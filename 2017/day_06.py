from utils import read, print_answers


def step(mem):
    val = max(mem)
    idx = mem.index(val)
    mem[idx] -= val
    d, m = divmod(val, len(mem))
    for i in range(len(mem)):
        mem[i] += d
    for i in range(m):
        mem[(idx + i + 1) % len(mem)] += 1


mem = [*map(int, read(2017, 6).split("\t"))]

history, seen = [], set()
while (state := tuple(mem)) not in seen:
    seen.add(state)
    history.append(state)
    step(mem)

a1 = len(seen)
a2 = len(seen) - history.index(state)

print_answers(a1, a2, day=6)  # 14029 2765
