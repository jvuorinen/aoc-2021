import numpy as np

with open("inputs/day_13.txt") as f:
    arrival, b = f.read().split()
buses = [(int(b), a) for a, b in enumerate(b.split(","), 0) if b != "x"]

wait_time = lambda ts, bus_id: (bus_id - ts % bus_id) % bus_id
f = lambda b: wait_time(int(arrival), b[0])
print(f"Part 1: {min(buses, key=f)[0] * min(map(f, buses))}")

ts, step = 0, 1
for b, c in buses:
    while wait_time(ts, b) != (c % b):
        ts += step
    step = np.lcm(step, b)
print(f"Part 2 {ts}")
