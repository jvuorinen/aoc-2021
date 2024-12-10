from utils import read, print_answers


def get_neighbors(node):
    candidates = [node + d for d in (1, -1, 1j, -1j)]
    return [c for c in candidates if c in M and M[c] - M[node] == 1]


def dfs(node, path=None, done=None):
    done = set() if done is None else done
    path = [] if path is None else path
    if node in ends:
        done.add(tuple(path))
        return
    for nn in get_neighbors(node):
        dfs(nn, path + [nn], done)
    trailheads = set(p[-1] for p in done)
    return len(trailheads), len(done)


raw = read(2024, 10).split("\n")

M = {c - 1j * r: int(x) for r, line in enumerate(raw) for c, x in enumerate(line)}
starts = [k for k, v in M.items() if v == 0]
ends = set([k for k, v in M.items() if v == 9])

a1, a2 = map(sum, zip(*[dfs(s) for s in starts]))

print_answers(a1, a2, day=10)
