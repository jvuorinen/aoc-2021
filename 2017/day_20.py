from collections import Counter
import numpy as np
import re
from utils import read, print_answers

raw = read(2017, 20).split("\n")

particles = np.array([[*map(int, re.findall(r"[-\d]+", line))] for line in raw])
a1 = abs(particles[:, 6:]).sum(axis=1).argmin()

for _ in range(1000):
    particles[:, 3:6] += particles[:, 6:]
    particles[:, :3] += particles[:, 3:6]
    locs = [tuple(p) for p in particles[:, :3]]
    cnt = Counter(locs)
    safe = [i for i, p in enumerate(locs) if cnt[p] == 1]
    particles = particles[safe, :]

a2 = len(particles)
print_answers(a1, a2, day=99)
