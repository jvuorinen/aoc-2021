from utils import read_input
import numpy as np


class CucumberHerd:
    def __init__(self, right, down) -> None:
        self.init_right = right
        self.init_down = down
        self.reset()

    def reset(self):
        self.right = self.init_right.copy()
        self.down = self.init_down.copy()
        self.finished = False
        self.turn = "right"
        self.i = 0

    def __repr__(self) -> str:
        arr = np.full(self.right.shape, fill_value=".")
        arr[self.right] = ">"
        arr[self.down] = "v"
        s = "\n".join("".join(x) for x in list(arr))
        return s

    def _move_right(self):
        dest = np.roll(self.right, 1, 1)
        occupied = self.right | self.down
        moved_new = dest & (~occupied)
        moved_old = np.roll(moved_new, -1, 1)
        not_moved = self.right & (~moved_old)
        self.right = not_moved | moved_new
        return moved_new.sum()

    def _move_down(self):
        dest = np.roll(self.down, 1, 0)
        occupied = self.right | self.down
        moved_new = dest & (~occupied)
        moved_old = np.roll(moved_new, -1, 0)
        not_moved = self.down & (~moved_old)
        self.down = not_moved | moved_new
        return moved_new.sum()

    def step(self):
        self.i += 1
        n = self._move_right()
        n += self._move_down()

        if n == 0:
            self.finished = True

        self.turn = "down" if self.turn == "right" else "right"


def get_cleaned_input():
    raw_in = read_input("inputs/day_25.txt")
    arr = np.array([list(x) for x in raw_in])

    herd_right = arr == ">"
    herd_down = arr == "v"

    herd = CucumberHerd(herd_right, herd_down)
    return herd


def solve(herd):
    herd.reset()
    while not herd.finished:
        herd.step()
    return herd.i


if __name__ == "__main__":
    herd = get_cleaned_input()

    answer_1 = solve(herd)

    print(f"Part 1 answer: {answer_1}")
