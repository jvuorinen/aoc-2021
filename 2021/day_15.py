from heapq import heappush, heappop

import numpy as np

from utils import read_input


def get_cleaned_input():
    raw_in = read_input("inputs/day_15.txt")
    inputs = np.array([list(line) for line in raw_in]).astype(int)
    return inputs


def add_coords(c1, c2):
    c = (c1[0] + c2[0], c1[1] + c2[1])
    return c


def is_within_bounds(coord, arr):
    dim_i, dim_j = arr.shape
    is_valid = (0 <= coord[0] < dim_i) & (0 <= coord[1] < dim_j)
    return is_valid


def get_neighbors(coord, arr):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    candidates = [add_coords(coord, c) for c in offsets]
    actions = set(c for c in candidates if is_within_bounds(c, arr))
    return actions


def enlarge_array(arr):
    add_h = np.tile(np.repeat(np.arange(5), len(arr)), (5 * len(arr), 1))
    add_v = np.tile(np.repeat(np.arange(5), len(arr)), (5 * len(arr), 1)).T
    addition = add_h + add_v
    raw = np.tile(arr, (5, 5)) + addition
    corr = ((raw - 1) // 9) * 9
    final = raw - corr

    return final


class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.entry_finder = {}
        self.counter = 0

    def __len__(self):
        return len(self.entry_finder)

    def __repr__(self):
        return str(self.entry_finder)

    def push(self, item, priority):
        """Add a new task or update the priority of an existing task"""

        if item in self.entry_finder:
            self._remove(item)
        self.counter += 1
        entry = [priority, self.counter, item]
        self.entry_finder[item] = entry
        heappush(self.pq, entry)

    def pop(self):
        """Remove and return the lowest priority task"""
        while self.pq:
            _, _, item = heappop(self.pq)
            if item != "<removed>":
                del self.entry_finder[item]
                return item

    def _remove(self, item):
        """Mark as removed"""
        entry = self.entry_finder.pop(item)
        entry[2] = "<removed>"


def solve(arr):
    INF = 9999
    end_coord = (arr.shape[0] - 1, arr.shape[1] - 1)

    distances = {(i, j): INF for i in range(arr.shape[0]) for j in range(arr.shape[1])}

    queue = PriorityQueue()
    queue.push((0, 0), 0)

    visited = set()
    distances[(0, 0)] = 0

    while len(queue) > 0:
        current = queue.pop()
        visited.add(current)

        if current == end_coord:
            return distances[current]

        for nb in get_neighbors(current, arr):
            if nb not in visited:
                new_distance = distances[current] + arr[nb]

                if new_distance < distances[nb]:
                    distances[nb] = new_distance
                    queue.push(nb, new_distance)


if __name__ == "__main__":
    arr = get_cleaned_input()
    enlarged = enlarge_array(arr)

    answer_1 = solve(arr)
    answer_2 = solve(enlarged)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
