from utils import read, print_answers

area, _dirs = read(2024, 15).split("\n\n")
dirs = [{"<": -1, ">": 1, "^": -1j, "v": 1j}[x] for x in _dirs.replace("\n", "")]


def has_box(p, boxes, part2):
    if not part2:
        return p in boxes
    return p in boxes or (p - 1) in boxes


def descendants(p, d, boxes, part2):
    if not part2:
        return [_p] if (_p := p + d) in boxes else []
    if d in (-1, 1):
        return [_p] if (_p := p + 2 * d) in boxes else []
    return [_p for dd in (-1, 0, 1) if (_p := p + d + dd) in boxes] or []


def build_stack(p, d, boxes, floor, stack, part2):
    if part2 and p - 1 in boxes:
        p -= 1
    if p not in boxes:
        return
    _p = p + d
    if (_p not in floor) or (part2 and (_p + 1 not in floor)):
        stack.clear()
        return
    stack.add(p)
    for _p in descendants(p, d, boxes, part2):
        if stack:
            build_stack(_p, d, boxes, floor, stack, part2)
    return stack or None


def solve(area, part2=False):
    if part2:
        area = area.replace("#", "##")
        area = area.replace("O", "[]")
        area = area.replace(".", "..")
        area = area.replace("@", "@.")

    M = {c + 1j * r: x for r, line in enumerate(area.split("\n")) for c, x in enumerate(line)}
    p = next(k for k, v in M.items() if v == "@")
    boxes = set([k for k, v in M.items() if v in "O["])
    floor = set([k for k, v in M.items() if v != "#"])

    for d in dirs:
        if p + d in floor and not has_box(p + d, boxes, part2):
            p += d
        else:
            stack = build_stack(p + d, d, boxes, floor, set(), part2)
            if stack:
                boxes -= stack
                boxes |= {b + d for b in stack}
                p += d

    return int(sum([100 * z.imag + z.real for z in boxes]))


a1 = solve(area, part2=False)
a2 = solve(area, part2=True)
print_answers(a1, a2, day=15)
# 1426855
# 1404917
