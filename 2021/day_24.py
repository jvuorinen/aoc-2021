import sys
import termios
import tty
from os import system

import numpy as np

from utils import read_input

# To make interactive session work properly
np.set_printoptions(linewidth=np.inf)
filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)


class ALU:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.w = [0]
        self.x = [0]
        self.y = [0]
        self.z = [0]
        self.input_buffer = []

    def read(self, i):
        self.input_buffer.insert(0, i)

    def load_program(self, program):
        self.program = program

    def run(self, inputs):
        self.reset()

        for i in inputs:
            self.read(i)

        for cmd in self.program:
            self.execute(cmd)

    def __repr__(self) -> str:
        s = f"w: {self.w} x: {self.x} y: {self.y} z:{self.z}\n"
        s += f"Inputs buffer: {self.input_buffer}"
        return s

    def execute(self, cmd):
        as_list = cmd.split()
        if len(as_list) == 2:
            instr, a = as_list
            a = self._determine_address(a)
        else:
            instr, a, b = as_list
            a = self._determine_address(a)
            b = self._determine_address(b)

        if instr == "inp":
            self._inp(a)
        elif instr == "add":
            self._add(a, b)
        elif instr == "mul":
            self._mul(a, b)
        elif instr == "div":
            self._div(a, b)
        elif instr == "mod":
            self._mod(a, b)
        elif instr == "eql":
            self._eql(a, b)

    def _determine_address(self, char):
        if char == "w":
            return self.w
        elif char == "x":
            return self.x
        elif char == "y":
            return self.y
        elif char == "z":
            return self.z
        else:
            return [int(char)]

    def _inp(self, a):
        a[0] = self.input_buffer.pop()

    def _add(self, a, b):
        a[0] = a[0] + b[0]

    def _mul(self, a, b):
        a[0] = a[0] * b[0]

    def _div(self, a, b):
        a[0] = a[0] // b[0]

    def _mod(self, a, b):
        a[0] = a[0] % b[0]

    def _eql(self, a, b):
        a[0] = 1 if (a[0] == b[0]) else 0


def get_cleaned_input():
    program = read_input("inputs/day_24.txt")
    return program


def check(alu):
    alu.run()

    for _ in range(14):
        for x in range(9, 0, -1):
            alu.run(x)
            if alu.z[0] == 1:
                yield x


def pad(s, width):
    n = width - len(s)
    return " " * n + s


def update_screen(code, alu, cursor):
    arr = np.full((9, 14), dtype="<U12", fill_value="==========")

    for place in range(len(code)):
        cp = code[:]
        for d in range(1, 10):
            cp[place] = d
            alu.run(cp)
            arr[d - 1, place] = pad(str(alu.z[0]), 10)

    for a, b in enumerate(code):
        arr[b - 1, a] = ">" + arr[b - 1, a][1:]

    arr_cursor = np.full(shape=(1, 14), dtype="<U12", fill_value="          ")
    arr_cursor[0, cursor] = "=========="
    final = np.vstack([arr_cursor, arr, arr_cursor])

    s = "\n".join("  ".join(x) for x in list(final))

    system("clear")
    print("The Interactive MONAD Cracker")
    print("(change code with 4,5,6,8 keys, quit by pressing q)")
    print(s)
    print("Current code:")
    print("".join(map(str, code)))


def run_interactive_session(code_str, alu):
    code = [int(x) for x in list(code_str)]
    cursor = 0

    while True:
        update_screen(code, alu, cursor)

        i = sys.stdin.read(1)[0]

        if i == "q":
            return
        elif i == "4":
            cursor -= 1
            cursor %= 14
        elif i == "6":
            cursor += 1
            cursor %= 14
        elif i == "5":
            d = code[cursor] + 1
            d = (d - 1) % 9 + 1
            code[cursor] = d
        elif i == "8":
            d = code[cursor] - 1
            d = (d - 1) % 9 + 1
            code[cursor] = d


if __name__ == "__main__":
    program = get_cleaned_input()

    alu = ALU()
    alu.load_program(program)

    run_interactive_session("55555555555555", alu)
