from utils import read_file, print_answers


def parse(raw_in):
    simple, hard = [], []
    for line in raw_in:
        a, b, c = line.split(" ")
        simple.append((a, int(b)))
        hard.append(("RDLU"[int(c[7:8])], int(c[2:7], 16)))
    return simple, hard


def get_area(instr):
    DIRS = {"R": 1, "L": -1, "D": 1j, "U": -1j}
    c = complex(0, 0)
    coords = [c]
    for hdg, n in instr:
        c += DIRS[hdg] * n
        coords.append(c)
    pairs = [*zip(coords[:-1], coords[1:])]
    area = abs(sum([(z1 * z2.conjugate()).imag for z1, z2 in pairs])) / 2
    perimeter = sum([abs(z1 - z2) for z1, z2 in pairs])
    return round(area + 1 + 0.5 * perimeter)


raw_in = read_file("inputs/day_18b.txt").split("\n")
simple, hard = parse(raw_in)

a1 = get_area(simple)
a2 = get_area(hard)

print_answers(a1, a2, day=18)  # Correct: 50465, 82712746433310
