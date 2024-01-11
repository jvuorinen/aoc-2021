from itertools import product

import matplotlib.pyplot as plt
import numpy as np

from utils import read_input


def draw(beacons, scanners):
    _ = plt.figure(figsize=(16, 16))
    ax = plt.axes(projection="3d")
    ax.scatter3D(beacons[:, 0], beacons[:, 1], beacons[:, 2])
    ax.scatter3D(scanners[:, 0], scanners[:, 1], scanners[:, 2], color="red")
    plt.show()


def parse_line(line):
    tmp = line.split("\n")
    beacons = np.array([list(map(int, x.split(","))) for x in tmp[1:]])
    return beacons


def get_cleaned_input():
    raw_in = read_input("inputs/day_19.txt", "\n\n")
    input_beacons = [parse_line(line) for line in raw_in]
    return input_beacons


def roll(points):
    return points[:, [0, 2, 1]] * [1, 1, -1]


def turn(points):
    return points[:, [1, 0, 2]] * [-1, 1, 1]


def get_orientations(points):
    for _ in range(2):
        for _ in range(3):
            points = roll(points)
            yield (points)
            for _ in range(3):
                points = turn(points)
                yield (points)
        points = roll(turn(roll(points)))


def combine(beacons, other_beacons, scanners):
    COMMON_NEEDED = 12
    set_a = set(map(tuple, beacons))

    for o in get_orientations(other_beacons):
        # This could probably be optimised... there is likely no need
        # to go through all possible combinations since likely the common
        # points lie on the fringes
        combinations = product(beacons, o)

        for a, b in combinations:
            shift = a - b
            set_shifted_o = set(map(tuple, o + shift))
            common = set_a & set_shifted_o

            if len(common) >= COMMON_NEEDED:
                combined = set_a | set_shifted_o
                updated_beacons = np.array(list(combined))
                updated_scanners = np.vstack([scanners, shift])
                return updated_beacons, updated_scanners, True

    return beacons, scanners, False


def build_map(input_beacons):
    beacons = input_beacons[0]
    scanners = np.array([[0, 0, 0]])
    idxes_to_combine = set(range(1, len(input_beacons)))

    n_total = len(input_beacons) - 1
    while idxes_to_combine:
        n_left = n_total - len(idxes_to_combine)
        print(f"Scanners combined: {n_left}/{len(input_beacons)}")

        for idx in idxes_to_combine:
            other_beacons = input_beacons[idx]
            beacons, scanners, success = combine(beacons, other_beacons, scanners)
            if success:
                idxes_to_combine.remove(idx)
                break

    return beacons, scanners


def manhattan_distance(a, b):
    result = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
    return result


def get_longest_distance(points):
    combinations = product(map(tuple, points), map(tuple, points))
    result = max(manhattan_distance(a, b) for a, b in combinations)
    return result


if __name__ == "__main__":
    input_beacons = get_cleaned_input()

    beacons, scanners = build_map(input_beacons)
    # draw(beacons, scanners)

    answer_1 = len(beacons)
    answer_2 = get_longest_distance(scanners)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
