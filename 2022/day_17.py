from utils import read_file, print_answers
import numpy as np
import os
import tty
import sys
from itertools import cycle


DOWN = (-1, 0)
LEFT = (0, 1)
RIGHT = (0, -1)
CMDS = {"<": LEFT, ">": RIGHT}


def run_interactive_session(tetris):
    tty.setcbreak(sys.stdin)

    while True:
        os.system("clear")
        print(tetris)

        match sys.stdin.read(1)[0]:
            case "q":
                return
            case "a":
                tetris.update(LEFT)
            case "d":
                tetris.update(RIGHT)


def parse_pieces(raw_in):
    parse = lambda x: (np.array([x for x in map(list, x.split("\n"))]) == "#").astype(int)
    return [np.flip(parse(x), axis=[0, 1]) for x in raw_in]


class Tetris:
    def __init__(self, width, pieces):
        self.field = np.zeros((10, width), dtype=int)
        self.pieces = pieces
        self.piece_idx = 0
        self.n_pieces = len(pieces)
        self.n_fallen = 0
        self.tick = 0
        self.width = width
        self.surface = 0

        self._spawn_candidate_piece()

    def __repr__(self):
        screen = self.field + 2 * self._get_candidate_field(self.candidate_loc)
        screen = np.flip(screen, axis=[0, 1])
        arr = np.array([".", "#", "@"])[screen]

        s = ""
        s += f"Tick: {self.tick}\n"
        s += f"Candidate loc: {self.candidate_loc}\n"
        s += "\n".join(map("".join, arr))
        return s

    def _spawn_candidate_piece(self):
        LOC_Y = self.surface + 3
        LOC_X = self.width - (self._get_candidate_piece().shape[1] + 2)
        self.candidate_loc = np.array([LOC_Y, LOC_X])

    def _get_candidate_field(self, candidate_loc):
        cfield = np.zeros_like(self.field)
        piece = self._get_candidate_piece()

        x, y = candidate_loc
        dx, dy = piece.shape
        cfield[x : x + dx, y : y + dy] += piece
        return cfield

    def _get_candidate_piece(self):
        return self.pieces[self.piece_idx]

    def _freeze_candidate(self):
        new = self.field + self._get_candidate_field(self.candidate_loc)
        self.field = new

    def _is_within_bounds(self, try_loc):
        piece = self._get_candidate_piece()
        return all(
            [
                try_loc[0] >= 0,
                try_loc[1] + (piece.shape[1] - 1) < self.width,
                try_loc[1] >= 0,
            ]
        )

    def _is_legal_move(self, move):
        try_loc = self.candidate_loc + move
        if not self._is_within_bounds(try_loc):
            return False
        else:
            cfield = self._get_candidate_field(try_loc)
            if bool((self.field + cfield > 1).sum()):
                return False
        return True

    def _update_surface(self):
        occupied = self.field.sum(axis=1) > 0
        if sum(occupied) == 0:
            self.surface = 0
        else:
            self.surface = np.argmax(~occupied)
            if sum(~occupied) < 8:
                self._extend_field()

    def _extend_field(self):
        AMOUNT = 12
        self.field = np.pad(self.field, pad_width=(0, AMOUNT))[:, :-AMOUNT]

    def _attempt_move(self, move):
        if self._is_legal_move(move):
            self.candidate_loc += move
            return True
        return False

    def update(self, move):
        self.tick += 1

        _ = self._attempt_move(move)

        success = self._attempt_move(DOWN)
        if not success:
            self.n_fallen += 1
            self._freeze_candidate()
            self._update_piece_idx()
            self._update_surface()
            self._spawn_candidate_piece()

    def _update_piece_idx(self):
        self.piece_idx = (self.piece_idx + 1) % self.n_pieces

    def get_surface_id(self, id_size):
        chunk = self.field[self.surface - id_size : self.surface]
        return tuple(tuple(x) for x in chunk)


def solve(pieces, commands, n_rocks):
    ID_SIZE = 8  # Gives a wrong answer if this is set too low

    tetris = Tetris(7, pieces)
    seen = {}
    cmd_cycle = cycle(enumerate(commands))
    pattern_found = False

    for cmd_idx, cmd in cmd_cycle:
        tetris.update(CMDS[cmd])

        if (not pattern_found) and (tetris.surface > ID_SIZE):
            tag = (cmd_idx, tetris.piece_idx, tetris.get_surface_id(ID_SIZE))
            if tag not in seen:
                seen[tag] = (tetris.n_fallen, tetris.surface)
            else:
                pattern_found = True
                now_r, now_h = tetris.n_fallen, tetris.surface
                prev_r, prev_h = seen[tag]

                repeats = (n_rocks - now_r) // (now_r - prev_r)

                n_rocks -= repeats * (now_r - prev_r)
                big_bulk = repeats * (now_h - prev_h)

        elif tetris.n_fallen == n_rocks:
            return tetris.surface + big_bulk


if __name__ == "__main__":
    pieces = parse_pieces(read_file("inputs/day_17pieces.txt").split("\n\n"))
    commands = list(read_file("inputs/day_17b.txt"))

    # tetris = Tetris(7, pieces)
    # run_interactive_session(tetris)

    a1 = solve(pieces, commands, 2022)
    a2 = solve(pieces, commands, 1000000000000)

    print_answers(a1, a2, day=17)
