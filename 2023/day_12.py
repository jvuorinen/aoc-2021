from utils import read_file, print_answers, memoize


def parse(raw_in):
    res = []
    for line in raw_in:
        txt, b = line.split(" ")
        bombs = tuple([int(x) for x in b.split(",")])
        res.append((txt, bombs))
    return res


def is_impossible(fumbled, bombs):
    if sum(bombs) > len(fumbled) - fumbled.count("."):
        return True


def get_actions(fumbled, bombs):
    actions = []
    if fumbled[0] == ".":
        return ["."]
    if fumbled[0] == "?":
        actions.append(".")
    if bombs:
        n = bombs[0]
        chunk = fumbled[:n]
        is_last_bomb = len(bombs) == 1
        last_char_ok = is_last_bomb or (fumbled[n] != "#")
        if "." not in chunk and last_char_ok:
            a = n * "#"
            if not is_last_bomb:
                a += "."
            actions.append(a)
    return sorted(actions)


def step(action, fumbled, bombs):
    f = fumbled[len(action) :]
    b = bombs[1:] if action[0] == "#" else bombs
    return f, b


@memoize
def _count(fumbled, bombs):
    if (len(fumbled) == 0) and len(bombs) == 0:
        return 1
    if is_impossible(fumbled, bombs):
        return 0
    if fumbled:
        cnt = 0
        for a in get_actions(fumbled, bombs):
            f, b = step(a, fumbled, bombs)
            cnt += _count(f, b)
        return cnt


def count(fumbled, bombs, multiply):
    fumbled = "?".join([fumbled] * multiply)
    bombs = bombs * multiply
    return _count(fumbled, bombs)


raw_in = read_file("inputs/day_12b.txt").split("\n")
parsed = parse(raw_in)

a1 = [count(f, b, 1) for f, b in parsed]
a2 = [count(f, b, 5) for f, b in parsed]

print_answers(sum(a1), sum(a2), day=12)  # Correct: 6852, 8475948826693
