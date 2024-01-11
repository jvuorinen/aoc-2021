from utils import read_input
import numpy as np


def get_cleaned_input():
    raw_in = read_input("inputs/day_07.txt")
    positions = [int(i) for i in raw_in[0].split(",")]
    return np.array(positions)


def triangular(x):
    result = (x * (x + 1)) / 2
    return result


def get_fuel_consumption(positions, func):
    consumptions = [sum(func(abs(x - positions))) for x in positions]
    return min(consumptions)


if __name__ == "__main__":
    positions = get_cleaned_input()

    c1 = get_fuel_consumption(positions, func=lambda x: x)
    c2 = get_fuel_consumption(positions, func=triangular)

    print(f"Part 1 answer: {c1}")
    print(f"Part 2 answer: {int(c2)}")
