from itertools import count

import numpy as np

from utils import read_input


def parse_input(raw_in):
    a, b = raw_in
    earliest = int(a)
    buses = [(int(b), a) for a, b in enumerate(b.split(","), 0) if b != "x"]
    return earliest, buses


def _get_wait_time(ts, bus_id):
    t = bus_id - ts % bus_id
    return t if t < bus_id else 0


def solve_1(earliest, buses):
    bus_ids = [b[0] for b in buses]
    wait_times = [_get_wait_time(earliest, b) for b in bus_ids]
    min_id = np.argmin(wait_times)
    return wait_times[min_id] * bus_ids[min_id]


def solve_2(buses):
    tstamp, step = 0, 1
    for bus_id, condition in buses:
        while _get_wait_time(tstamp, bus_id) != (condition % bus_id):
            tstamp += step
        step = np.lcm(step, bus_id)
    return tstamp


if __name__ == "__main__":
    raw_in = read_input("inputs/day_13.txt")
    earliest, buses = parse_input(raw_in)

    answer_1 = solve_1(earliest, buses)
    answer_2 = solve_2(buses)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
