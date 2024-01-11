from utils import read_file, print_answers
import numpy as np
from dataclasses import dataclass
from collections import defaultdict


def _get_range(x1, x2):
    return range(min(x1, x2), max(x1, x2) + 1)


def _interpolate(a, b):
    (aa, ab), (ba, bb) = a, b
    if aa == ba:
        return set([(aa, d) for d in _get_range(ab, bb)])
    elif ab == bb:
        return set([(d, ab) for d in _get_range(aa, ba)])


def _get_points(line):
    corners = [tuple(map(int, x.split(","))) for x in line.split(" -> ")]
    pairs = [p for p in zip(corners[:-1], corners[1:])]
    return set.union(*[_interpolate(*p) for p in pairs])


@dataclass
class Thingy:
    depth: int
    symbol: str

    def __repr__(self) -> str:
        return f"{self.symbol} (depth: {self.depth})"


@dataclass
class Shaft:
    thingies: list[Thingy]
    occupied: set[int]

    def __init__(self) -> None:
        self.thingies = []
        self.occupied = set()

    def _sort(self):
        self.thingies = sorted(self.thingies, key=lambda t: t.depth)

    def is_occupied(self, depth: int):
        return depth in self.occupied

    def insert(self, idx, t: Thingy):
        self.thingies.insert(idx, t)
        self.occupied.add(t.depth)

    def get_max_depth(self):
        return max([t.depth for t in self.thingies])


@dataclass
class Shaftery:
    shafts: dict[int, Shaft]
    drops: int = 0
    end_reached: bool = False

    def __repr__(self) -> str:
        return "\n".join([f"{i}: {sh.thingies}" for i, sh in self.shafts.items()])

    def _shaft_available(self, shaft: int, depth: int):
        return (shaft in self.shafts) and not self.shafts[shaft].is_occupied(depth)

    def drop_item(self, shaft: int, depth, symbol: str):
        if self.end_reached:
            return
        sh = self.shafts[shaft]

        for i, t in enumerate(sh.thingies):
            if t.depth > depth:
                left, right = shaft - 1, shaft + 1
                for _sh in left, right:
                    if _sh not in self.shafts:
                        self.end_reached = True
                        return
                    if not self.shafts[_sh].is_occupied(t.depth):
                        self.drop_item(_sh, t.depth, symbol)
                        return
                self.drops += 1
                sh.insert(i, Thingy(t.depth - 1, symbol))
                return
        self.end_reached = True

    def get_max_depth(self):
        return max([s.get_max_depth() for s in self.shafts.values()])

    def draw(self):
        max_d = self.get_max_depth()
        arr = np.zeros((max_d + 1, len(self.shafts)), dtype=str)
        arr[:, :] = "."
        for i, sh in enumerate(self.shafts.values()):
            for t in sh.thingies:
                arr[t.depth, i] = t.symbol
        arr = np.flip(arr, axis=1)
        print("\n".join(map("".join, arr)))


def create_shaftery(coords, floor=bool):
    FLOOR_BOUNDS = 0, 1000

    d = defaultdict(Shaft)
    if floor:
        fy = max([c[1] for c in coords]) + 2
        for fx in range(*FLOOR_BOUNDS):
            d[fx].insert(0, Thingy(fy, "#"))

    for x, y in coords:
        d[x].insert(0, Thingy(y, "#"))

    ordered = {k: v for k, v in sorted(d.items())}
    for sh in ordered.values():
        sh._sort()
    return Shaftery(shafts=ordered)


def _quit_simulation(shaftery, start_shaft):
    start_shaft_occupied = shaftery.shafts[start_shaft].is_occupied(0)
    return start_shaft_occupied or shaftery.end_reached


def simulate(coords, floor: bool):
    START_SHAFT = 500
    shaftery = create_shaftery(coords, floor=floor)

    while not _quit_simulation(shaftery, START_SHAFT):
        shaftery.drop_item(START_SHAFT, 0, "o")
    # shaftery.draw()

    return shaftery.drops


if __name__ == "__main__":
    raw_in = read_file("inputs/day_14b.txt").split("\n")
    coords = set.union(*[_get_points(line) for line in raw_in])

    a1 = simulate(coords, floor=False)
    a2 = simulate(coords, floor=True)

    print_answers(a1, a2, day=14)
