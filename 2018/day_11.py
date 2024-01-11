import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from utils import print_answers

SERIAL = 9810
SIZE = 300
STOP_AT_SIZE = 30

x, y = np.meshgrid(np.arange(SIZE + 1), np.arange(SIZE + 1))
rack_id = x + 10
power = (rack_id * y + SERIAL) * rack_id
lvl = (power // 100) % 10 - 5

best = 0
for size in range(3, STOP_AT_SIZE):
    totals = sliding_window_view(lvl, (size, size)).sum(axis=(2, 3))
    ymax, xmax = np.unravel_index(totals.argmax(), totals.shape)
    if size == 3:
        a1 = f"{xmax},{ymax}"
    if totals.max() > best:
        a2 = f"{xmax},{ymax},{size}"
        best = totals.max()

print_answers(a1, a2, day=11)
