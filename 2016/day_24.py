from utils import read, print_answers


def bfs(num):
    start = next(k for k, v in M.items() if v == num)
    todo = [(0, start)]
    ok = floor - {start}
    res = {}
    for i, n in todo:
        if i > 0 and (k := M.get(n, "")).isnumeric():
            res[k] = i
        for nn in (n + 1, n - 1, n + 1j, n - 1j):
            if nn in ok:
                ok.remove(nn)
                todo.append((i + 1, nn))
    return res


def crawl(node, todo, s=0, part2=False):
    if not todo:
        return s + part2 * (D[node]["0"])
    return min(crawl(n, todo - {n}, s + D[node][n], part2) for n in todo)


raw = read(2016, 24).split("\n")

M = {c - 1j * r: x for r, line in enumerate(raw) for c, x in enumerate(line)}
floor = {k for k, v in M.items() if v != "#"}
nums = {v for v in M.values() if v.isdigit()}

D = {n: bfs(n) for n in nums}

a1 = crawl("0", nums - {"0"}, part2=False)
a2 = crawl("0", nums - {"0"}, part2=True)
print_answers(a1, a2, day=24)
