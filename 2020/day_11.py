from functools import lru_cache
from itertools import count

from utils import print_array, read_input, str_to_array

import numpy as np


class Ferry:
    def __init__(self, seatmap):
        self.area = seatmap.copy()
        self.max_i, self.max_j = seatmap.shape

    def draw(self):
        print_array(self.area)

    def count_occupied(self):
        return (self.area == ord("#")).sum().sum()

    def _is_within_limits(self, cell):
        return (0 <= cell[0] <= self.max_i - 1) & (0 <= cell[1] <= self.max_j - 1)

    @lru_cache(maxsize=None)
    def _get_neighbors_simple(self, cell):
        i, j = cell
        candidates = [(i + a, j + b) for a in (-1, 0, 1) for b in (-1, 0, 1)]
        valid = [c for c in candidates if self._is_within_limits(c) & (c != (i, j))]
        return valid

    @lru_cache(maxsize=None)
    def _get_neighbors_complex(self, cell):
        # Travel along the 8 lines in turn until a seat is found
        i, j = cell
        neighbors = []
        directions = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if not (a == b == 0)]
        for a, b in directions:
            for r in count(1):
                candidate = (i + a * r, j + b * r)
                if not self._is_within_limits(candidate):
                    break
                elif self.area[candidate] in (ord("L"), ord("#")):
                    neighbors.append(candidate)
                    break
        return neighbors

    def _neighbors_over_limit(self, cell, method, limit):
        cells = method(cell)
        s = 0
        for c in cells:
            if self.area[c] == ord("#"):
                s += 1
            if s > limit:
                return True
        return False

    def _step(self, use_complex_method):
        if use_complex_method:
            method = self._get_neighbors_complex
            tolerance = 4
        else:
            method = self._get_neighbors_simple
            tolerance = 3

        a = self.area.copy()
        for i in range(0, self.max_i):
            for j in range(0, self.max_j):
                seat = i, j
                if self.area[seat] == ord("."):
                    continue
                elif (self.area[seat] == ord("L")) & ~self._neighbors_over_limit(seat, method, 0):
                    a[seat] = ord("#")
                elif (self.area[seat] == ord("#")) & self._neighbors_over_limit(
                    seat, method, tolerance
                ):
                    a[seat] = ord("L")

        self.area = a.copy()

    def simulate(self, use_complex_method):
        n_occupied = -99
        for i in count(1):
            self._step(use_complex_method)
            nxt = self.count_occupied()
            if nxt != n_occupied:
                n_occupied = nxt
            else:
                # print(f"Finished on iteration {i}")
                return n_occupied


def solve(seatmap, use_complex_method):
    f = Ferry(seatmap)
    res = f.simulate(use_complex_method)
    return res


if __name__ == "__main__":
    raw_in = read_input("inputs/day_11.txt")
    seatmap = str_to_array(raw_in)

    answer_1 = solve(seatmap, use_complex_method=False)
    answer_2 = solve(seatmap, use_complex_method=True)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
