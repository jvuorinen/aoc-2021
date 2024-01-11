import logging
import numpy as np

CHARS = {n: chr(n) for n in range(256)}


def read_input(fp, split_delimiter="\n"):
    logging.info("Reading file: " + fp)
    with open(fp) as fh:
        result = fh.read()
    return result.split(split_delimiter)


def memoize(func):
    mem = {}

    def inner(*args):
        mem_key = tuple(args)
        if mem_key not in mem:
            mem[mem_key] = func(*args)
        return mem[mem_key]

    return inner


def coords_to_array(coords):
    """Makes a np array out of coodinates"""
    # Shift coords to avoid negatives
    x_shift = abs(min(i[0] for i in coords.keys()))
    y_shift = abs(min(i[1] for i in coords.keys()))

    cells = {(k[0] + x_shift, k[1] + y_shift): v for k, v in coords.items()}

    # Create a numpy array from coordinate information
    # Note how x and y are represented in a np array
    x_max, y_max = map(max, zip(*cells.keys()))
    a = np.empty(shape=(y_max + 1, x_max + 1)).astype(int)
    a[:] = -1
    for (x, y), v in cells.items():
        a[y_max - y, x] = v

    return a


def str_to_array(raw_in):
    """Transforms a string representation of an
    ascii coord array into a np array"""
    as_list = [list(l) for l in raw_in]
    tmp = [list(map(ord, l)) for l in as_list]
    return np.array(tmp)


def array_to_string(a, conversion=CHARS):
    """Transforms ascii coord array to a string representation"""
    # conversion = {-1: "░", 0:"▓", 1: " ", 2:"€", 3:"@", 4:"S"}
    return "\n".join("".join(conversion.get(t, " ") for t in line) for line in a.tolist())


def print_array(a, conversion=CHARS):
    """Prints an ascii array to the screen"""
    print(array_to_string(a, conversion))


def chunked(l, n, no_overlap=True):
    """Yield successive n-sized chunks from l."""
    if no_overlap:
        for i in range(0, len(l), n):
            yield l[i : i + n]
    else:
        for i in range(0, len(l) - n):
            yield l[i : i + n]
