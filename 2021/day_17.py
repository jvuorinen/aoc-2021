import re
from itertools import product

import numpy as np

from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_17.txt")[0]

    xmin, xmax = map(int, (re.findall("x=(-?\d*)..(-?\d*)", raw_in)[0]))
    ymin, ymax = map(int, (re.findall("y=(-?\d*)..(-?\d*)", raw_in)[0]))

    # Assuming x-range does not cross origin
    # mirror the values if they are negative
    if xmin < 0:
        xmin *= -1
        xmax *= -1

    return (xmin, xmax, ymin, ymax)


def shoot(velocity, target):
    (
        x,
        y,
    ) = (0, 0)
    dx, dy = velocity
    top_y = 0

    while True:
        x += dx
        y += dy
        dy -= 1
        dx -= np.sign(dx)
        top_y = max(y, top_y)

        # In target area
        if (target[0] <= x <= target[1]) and (target[2] <= y <= target[3]):
            return {"velocity": velocity, "success": True, "top_y": top_y}

        # Out of range
        elif (x > target[1]) or (y < target[2]):
            return {"velocity": velocity, "success": False, "top_y": top_y}

        # Not enough dx left to reach target area
        elif (dx == 0) & (x < target[0]):
            return {"velocity": velocity, "success": False, "top_y": top_y}


if __name__ == "__main__":
    target = get_cleaned_input()

    # Certain over and undershoot limits
    x_low = 1
    x_high = target[1] + 1
    y_low = target[2]
    y_high = abs(target[2])

    velocity_tryouts = product(range(x_low, x_high), range(y_low, y_high))

    results = [shoot(v, target) for v in velocity_tryouts]
    successes = [r for r in results if r["success"]]

    answer_1 = max(r["top_y"] for r in successes)
    answer_2 = len(successes)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
