from utils import read, print_answers

cmds = read(2016, 1).split(", ")

visited = set()
found = False
loc, hdg = 0, 0
for cmd in cmds:
    hdg *= (1j, -1j)[cmd[0] == "R"]
    for _ in range(int(cmd[1:])):
        if not found and loc in visited:
            found = True
            hq = loc
        visited.add(loc)
        loc += hdg

a1 = int(abs(loc.real) + abs(loc.imag))
a2 = int(abs(hq.real) + abs(hq.imag))
print_answers(a1, a2, day=1)
