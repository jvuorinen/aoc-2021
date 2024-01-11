from functools import reduce
from itertools import cycle
from operator import mul

import numpy as np

from utils import array_to_string, read_input, str_to_array

OPPOSITE_HDG = {"n": "s", "e": "w", "s": "n", "w": "e"}


class Tile:
    def __init__(self, id, array):
        self.id = id
        self.arr = array

    def __repr__(self):
        return f"Tile {self.id}\n{array_to_string(self.arr)}"

    def rotate(self):
        self.arr = np.rot90(self.arr)

    def flip(self):
        self.arr = np.flip(self.arr, axis=1)

    def get_edges(self):
        return {
            "n": "".join(map(chr, self.arr[0, :])),
            "s": "".join(map(chr, self.arr[-1, :])),
            "w": "".join(map(chr, self.arr[:, 0])),
            "e": "".join(map(chr, self.arr[:, -1])),
        }


def create_tiles_dict(raw_in):
    tiles_dict = {}

    for line in raw_in:
        a, b = line.split("\n", maxsplit=1)
        a = int(a[5:-1])
        b = str_to_array(b.split())
        tiles_dict[a] = Tile(a, b)

    return tiles_dict


def find_corner_tiles(tiles_dict):
    # Corner pieces have exactly 2 sides that have a match in other tiles
    tiles = list(tiles_dict.values())
    corner_pieces = []
    for t in tiles:
        n_matches = 0
        for e in t.get_edges().values():
            edges_to_test = set.union(*(set(t2.get_edges().values()) for t2 in tiles if (t != t2)))
            edges_to_test_flipped = set(x[::-1] for x in edges_to_test)
            if (e in edges_to_test) or (e in edges_to_test_flipped):
                n_matches += 1
        if n_matches == 2:
            corner_pieces.append(t.id)
    return corner_pieces


def _find_match(tile, hdg, unsolved_tiles, tiles_dict):
    opp_hdg = OPPOSITE_HDG[hdg]
    for tile_id in unsolved_tiles:
        other = tiles_dict[tile_id]
        for _ in range(2):
            for _ in range(4):
                if tile.get_edges()[hdg] == other.get_edges()[opp_hdg]:
                    return other
                other.rotate()
            other.flip()


def piece_together(tiles_dict, corner_tiles):
    # Resources
    LOC_OFFSET = {
        "n": np.array([-1, 0]),
        "e": np.array([0, 1]),
        "s": np.array([1, 0]),
        "w": np.array([0, -1]),
    }
    hdg_iter = cycle(["e", "s", "w", "n"])

    # Init
    unsolved_tiles = set(tiles_dict)
    solution = {}
    loc = np.array([0, 0])
    hdg = next(hdg_iter)
    tile = tiles_dict[corner_tiles[0]]
    unsolved_tiles.remove(tile.id)

    # Loop and build the solution dict
    while unsolved_tiles:
        solution[tuple(loc)] = tile
        match = _find_match(tile, hdg, unsolved_tiles, tiles_dict)
        if match:
            tile = match
            unsolved_tiles.remove(tile.id)
            loc += LOC_OFFSET[hdg]

        if not match:
            hdg = next(hdg_iter)
    solution[tuple(loc)] = tile

    # Transform solution dict into a big tile
    row_idxes, col_idxes = zip(*solution.keys())
    row_min, row_max = min(row_idxes), max(row_idxes)
    col_min, col_max = min(col_idxes), max(col_idxes)
    rows = []
    for col in range(col_min, col_max + 1):
        rows.append(
            np.concatenate(
                [solution[(row, col)].arr[1:-1, 1:-1] for row in range(row_min, row_max + 1)],
                axis=0,
            )
        )
    final = np.concatenate(rows, axis=1)

    return Tile("FINALE", final)


def _calculate_roughness(array):
    monster_ascii = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    monster_filter = (str_to_array(monster_ascii) == ord("#")).astype(int)
    m_len_y, m_len_x = monster_filter.shape

    hashes = (array == ord("#")).astype(int)

    solution = np.zeros_like(hashes)
    max_y, max_x = solution.shape
    for row in range(0, max_y - m_len_y + 1):
        for col in range(0, max_x - m_len_x + 1):
            original = hashes[row : row + m_len_y, col : col + m_len_x]
            filtered = original * monster_filter
            if np.array_equal(filtered, monster_filter):
                solution[row : row + m_len_y, col : col + m_len_x] += filtered

    roughness = np.sum((solution == 0) * hashes)
    return roughness


def determine_roughness(tiles_dict, corner_tiles):
    final = piece_together(tiles_dict, corner_tiles)

    roughnesses = []
    for _ in range(2):
        final.flip()
        for _ in range(4):
            final.rotate()
            r = _calculate_roughness(final.arr)
            roughnesses.append(r)

    return min(roughnesses)


if __name__ == "__main__":
    raw_in = read_input("inputs/day_20.txt", split_delimiter="\n\n")
    tiles_dict = create_tiles_dict(raw_in)

    corner_tiles = find_corner_tiles(tiles_dict)
    roughness = determine_roughness(tiles_dict, corner_tiles)

    print(f"Part 1 answer: {reduce(mul, corner_tiles)}")
    print(f"Part 2 answer: {roughness}")
