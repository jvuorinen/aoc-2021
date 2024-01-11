from utils import read_file, print_answers, get_neighbors


def solve_1(cubes):
    count = lambda c: len([n for n in get_neighbors(c) if n not in cubes])
    return sum([count(c) for c in cubes])


def _get_initial_and_bounds(cubes):
    nums = set.union(*[set(c) for c in cubes])
    bmin, bmax = min(nums) - 2, max(nums) + 2

    initial = (bmin, bmin, bmin)
    bounds = [(bmin, bmax), (bmin, bmax), (bmin, bmax)]
    return initial, bounds


def solve_2(cubes):
    initial, bounds = _get_initial_and_bounds(cubes)

    visited = set(initial)
    Q = [initial]
    s = 0
    while Q:
        c = Q.pop(0)
        for n in get_neighbors(c, bounds):
            if n in cubes:
                s += 1
            elif n not in visited:
                visited.add(n)
                Q.append(n)
    return s


if __name__ == "__main__":
    raw_in = read_file("inputs/day_18b.txt").split()

    cubes = set(tuple(map(int, x.split(","))) for x in raw_in)

    a1 = solve_1(cubes)
    a2 = solve_2(cubes)

    print_answers(a1, a2, day=18)
