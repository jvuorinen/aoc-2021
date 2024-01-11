import numpy as np
from tqdm import tqdm

from utils import read_input


def get_neigborhood(i, j):
    return [(i + di, j + dj) for di in [-1, 0, 1] for dj in [-1, 0, 1]]


def bool_list_to_int(bl):
    s = "".join("1" if b else "0" for b in bl)
    return int(s, 2)


class ScannerImage:
    def __init__(self, in_enhancer, in_arr) -> None:
        self.in_enhancer = in_enhancer
        self.in_arr = in_arr
        self.reset()

    def reset(self):
        self.inf_value = False
        self.enhancer = self.in_enhancer[:]
        self.ones = set(zip(*np.where(self.in_arr)))
        self._update_index_ranges()

    def __repr__(self) -> str:
        # TODO remove coords => matrix into a separate function
        i_min, j_min, i_max, j_max = self.index_ranges

        i_dim = i_max - i_min
        j_dim = j_max - j_min

        arr = np.zeros((i_dim, j_dim), dtype=bool)

        for i in range(i_dim):
            for j in range(j_dim):
                v = self._get_value(i + i_min, j + j_min)
                arr[i, j] = v

        s_arr = np.full((i_dim, j_dim), fill_value=".")
        s_arr[np.where(arr)] = "#"

        s = "\n".join("".join(x) for x in list(s_arr))
        return s

    def _update_inf_value(self):
        key_bin = [self.inf_value for _ in range(9)]
        key = bool_list_to_int(key_bin)
        self.inf_value = bool(self.enhancer[key])

    def _get_value(self, i, j):
        i_min, j_min, i_max, j_max = self.index_ranges

        if (i_min <= i <= i_max) and (j_min <= j <= j_max):
            return (i, j) in self.ones
        else:
            return self.inf_value

    def _get_enhanced_value(self, i, j):
        nbs = get_neigborhood(i, j)
        key_bin = [self._get_value(*c) for c in nbs]
        key = bool_list_to_int(key_bin)
        enhanced = self.enhancer[key]

        return enhanced

    def _update_index_ranges(self):
        i_min = min(x[0] for x in self.ones)
        j_min = min(x[1] for x in self.ones)
        i_max = max(x[0] for x in self.ones)
        j_max = max(x[1] for x in self.ones)
        self.index_ranges = (i_min, j_min, i_max, j_max)

    def enhance(self):
        i_min, j_min, i_max, j_max = self.index_ranges

        to_enhance = {
            (i, j) for i in range(i_min - 5, i_max + 5) for j in range(j_min - 5, j_max + 5)
        }

        enhanced = {c for c in to_enhance if (self._get_enhanced_value(*c) == True)}
        self.ones = enhanced

        self._update_inf_value()
        self._update_index_ranges()


def get_cleaned_input():
    a, b = read_input("inputs/day_20.txt", "\n\n")
    enhancer_raw = "".join(a.split("\n"))
    img_raw = list(map(list, b.split("\n")))

    enhancer = [True if x == "#" else False for x in enhancer_raw]
    arr = (np.array(img_raw) == "#").astype(bool)

    img = ScannerImage(enhancer, arr)
    return img


def solve(img, n_steps):
    img.reset()

    for _ in tqdm(range(n_steps), ascii=True, ncols=80):
        img.enhance()

    n = len(img.ones)
    return n


if __name__ == "__main__":
    img = get_cleaned_input()

    answer_1 = solve(img, 2)
    answer_2 = solve(img, 50)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
