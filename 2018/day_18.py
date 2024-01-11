from utils import read, print_answers


def parse(file):
    rows = read(file).split("\n")
    grid = {x + y * 1j: c for y, row in enumerate(rows) for x, c in enumerate(row)}
    adj = {
        c: [_c for r in (-1, 0, 1) for i in (-1j, 0j, 1j) if (_c := c + r + i) != c and _c in grid]
        for c in grid
    }
    return grid, adj


def get_next(c, grid, adj):
    ns = [grid[n] for n in adj[c]]
    match grid[c]:
        case ".":
            return "|" if ns.count("|") >= 3 else "."
        case "|":
            return "#" if ns.count("#") >= 3 else "|"
        case "#":
            return "#" if ("#" in ns) and ("|" in ns) else "."


def find_cycle(grid, adj):
    history = []
    while (token := "".join(grid.values())) not in history:
        history.append(token)
        grid = {c: get_next(c, grid, adj) for c in grid}
    idx = history.index(token)
    return history[:idx], history[idx:]


def get_value(start, cycle, idx):
    tk = start[idx] if (idx <= len(start)) else cycle[(idx - len(start)) % len(cycle)]
    return tk.count("|") * tk.count("#")


grid, adj = parse("inputs/day_18b.txt")
start, cycle = find_cycle(grid, adj)

a1 = get_value(start, cycle, 10)
a2 = get_value(start, cycle, 1000000000)

print_answers(a1, a2, day=18)  # 539682, 226450
