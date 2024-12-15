from utils import read, print_answers

area, _dirs = read(2024, 15).split("\n\n")
dirs = [{"<": -1, ">": 1, "^": -1j, "v": 1j}[x] for x in _dirs.replace("\n", "")]


def get_box(p, boxes, part2):
    if p in boxes:
        return p
    if part2 and (p-1) in boxes:
        return (p-1)


def descendants(p, d, boxes, part2):
    if not part2:
        return [_p] if (_p := p + d) in boxes else []
    if d in (-1, 1):
        return [_p] if (_p := p + 2 * d) in boxes else []
    return [_p for dd in (-1, 0, 1) if (_p := p + d + dd) in boxes] or []


def build_stack(p, d, boxes, walls, stack, part2):
    _p = p + d
    if (_p in walls) or (part2 and (_p + 1 in walls)):
        stack.clear()
        return
    stack.add(p)
    for _p in descendants(p, d, boxes, part2):
        if stack:
            build_stack(_p, d, boxes, walls, stack, part2)
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
    walls = set([k for k, v in M.items() if v == "#"])

    for d in dirs:
        _p = p + d
        if _p in walls:
            continue
        elif b := get_box(_p, boxes, part2):
            stack = build_stack(b, d, boxes, walls, set(), part2)
            if stack:
                boxes -= stack
                boxes |= {b + d for b in stack}
                p = _p
        else:
            p = _p

    return int(sum([100 * z.imag + z.real for z in boxes]))


a1 = solve(area, part2=False)
a2 = solve(area, part2=True)
print_answers(a1, a2, day=15)
