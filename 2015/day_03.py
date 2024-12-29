from utils import read, print_answers

dirs = read(2015, 3)
D = (-1, 1, 1j, -1j)

simple = [p := 0] + [p := p + D["<>^v".index(c)] for c in dirs]
santa = [p := 0] + [p := p + D["<>^v".index(c)] for c in dirs[::2]]
robo = [p := 0] + [p := p + D["<>^v".index(c)] for c in dirs[1::2]]

a1 = len(set(simple))
a2 = len(set(santa) | set(robo))
print_answers(a1, a2, day=3)
