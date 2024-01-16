from utils import read, print_answers


def dance(word, cmds):
    prgs = list(word)
    for cmd in cmds:
        c, rest = cmd[0], cmd[1:]
        if c == "s":
            i = int(rest)
            prgs[:] = prgs[-i:] + prgs[:-i]
        if c == "x":
            a, b = map(int, rest.split("/"))
            prgs[a], prgs[b] = prgs[b], prgs[a]
        if c == "p":
            ia, ib = map(prgs.index, rest.split("/"))
            prgs[ia], prgs[ib] = prgs[ib], prgs[ia]
    return "".join(prgs)


def dance_much(word, cmds, times):
    seen = []
    while word not in seen:
        seen.append(word)
        word = dance(word, cmds)
    return seen[times % len(seen)]


cmds = read(2017, 16).split(",")
word = "abcdefghijklmnop"

a1 = dance(word, cmds)
a2 = dance_much(word, cmds, int(1e9))

print_answers(a1, a2, day=16)  # nlciboghjmfdapek nlciboghmkedpfja
