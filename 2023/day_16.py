from dataclasses import dataclass
from utils import print_answers, read_file


@dataclass
class Beam:
    loc: complex
    hdg: complex


def get_token(beam):
    return (beam.loc, beam.hdg)


def is_inside(i, j, area):
    return 0 <= i < len(area) and 0 <= j < len(area[0])


def simulate(beam, area):
    beams, visited = [beam], set()
    while beams:
        _beams = []
        for b in beams:
            b.loc += b.hdg
            i, j = int(b.loc.imag), int(b.loc.real)
            token = get_token(b)

            if (token not in visited) and is_inside(i, j, area):
                visited.add(token)
                _beams.append(b)

                match b.hdg, area[i][j]:
                    case 1 | -1, "/":
                        b.hdg *= -1j
                    case 1j | -1j, "/":
                        b.hdg *= 1j
                    case 1 | -1, "\\":
                        b.hdg *= 1j
                    case 1j | -1j, "\\":
                        b.hdg *= -1j
                    case 1 | -1, "|":
                        b.hdg = 1j
                        _beams.append(Beam(b.loc, -1j))
                    case 1j | -1j, "-":
                        b.hdg = 1
                        _beams.append(Beam(b.loc, -1))
        beams[:] = _beams
    return len(set([v[0] for v in visited]))


def find_best(area):
    rng_i, rng_j = range(len(area)), range(len(area[0]))
    starts = (
        [Beam(complex(-1, x), 1) for x in rng_j]
        + [Beam(complex(-1, x), 1) for x in rng_j]
        + [Beam(complex(x, -1), 1j) for x in rng_i]
        + [Beam(complex(x, len(area)), -1j) for x in rng_i]
    )
    return max([simulate(b, area) for b in starts])


if __name__ == "__main__":
    area = read_file("inputs/day_16b.txt").split()

    a1 = simulate(Beam(-1, 1), area)
    a2 = find_best(area)

    print_answers(a1, a2, day=16)  # Correct: 6994, 7488
