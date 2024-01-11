from utils import read_file, print_answers
from collections import defaultdict


def _get_key(st, name):
    return "/".join(st + [name])


def parse_filesystem(lines):
    fs = defaultdict(list)
    curr = "root"
    st = []

    for line in lines[1:]:
        curr_key = _get_key(st, curr)
        match line.split(" "):
            case "$", "cd", "..":
                curr = st.pop()
            case "$", "cd", to:
                st.append(curr)
                curr = to
            case "$", "ls":
                pass
            case "dir", dname:
                new_key = f"{curr_key}/{dname}"
                fs[curr_key].append(new_key)
            case size, _:
                fs[curr_key].append(int(size))
    return fs


def disk_usage(fs, directory):
    sizes = [x if isinstance(x, int) else disk_usage(fs, x) for x in fs[directory]]
    return sum(sizes)


if __name__ == "__main__":
    lines = read_file("inputs/day_07b.txt").split("\n")
    fs = parse_filesystem(lines)

    # Part 1
    sizes = [disk_usage(fs, d) for d in fs]
    a1 = sum(x for x in sizes if x <= 100_000)

    # Part 2
    available = 70_000_000 - disk_usage(fs, "root")
    needed = 30_000_000 - available
    a2 = min([x for x in sizes if x >= needed])

    print_answers(a1, a2, day=7)
