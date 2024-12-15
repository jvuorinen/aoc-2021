from utils import read, print_answers

# a, b = read().split("\n\n")
area, b = read(2024, 15).split("\n\n")
dirs = [{'<': -1, '>': 1, '^': -1j, 'v': 1j}[x] for x in b.replace("\n", "")]

def solve(area, part2=False):
    if part2:
        area = area.replace("#", "##")
        area = area.replace("O", "[]")
        area = area.replace(".", "..")
        area = area.replace("@", "@.")

    M = {c + 1j * r: x for r, line in enumerate(area.split('\n')) for c, x in enumerate(line)}

    p = next(k for k, v in M.items() if v == '@')
    barrels = set([k for k, v in M.items() if v == '['])
    floor = set([k for k, v in M.items() if v != '#'])

    def _get_stack(p, d, stack):
        if part2 and p - 1 in barrels:
            p -= 1
        if p not in barrels:
            return
        _p = p + d
        if (_p not in floor) or (_p + 1 not in floor):
            stack.clear()
            return
        stack.add(p)

        if d in (1, -1):
            if stack and _p + d in barrels:
                _get_stack(_p + d, d, stack)
        else:
            if stack and _p - 1 in barrels:
                _get_stack(_p - 1, d, stack)
            if stack and _p in barrels:
                _get_stack(_p, d, stack)
            if stack and _p + 1 in barrels:
                _get_stack(_p + 1, d, stack)
        return stack or None

    for d in dirs:
        if p + d in floor and (p+d) not in barrels and (p+d-1) not in barrels:
            p += d
        else:
            stack = _get_stack(p+d, d, set())
            if stack:
                barrels -= stack
                barrels |= {b + d for b in stack}
                p += d

    return int(sum([100*z.imag + z.real for z in barrels]))

a1 = None
a2 = solve(area, part2=True)
print_answers(a1, a2, day=15)
# 1426855
# 1404917