from utils import read_input

parse_addr = lambda cmd: f"{int(cmd[4:-1]):036b}"


def get_address_variations(addr, mask):
    addresses = []
    nbits = mask.count("X")
    base = [bin(i)[2:].zfill(nbits) for i in range(0, 2**nbits)]
    for b in base:
        it = iter(b)
        b_loc = "".join([a if m != "X" else next(it) for a, m in zip(addr, mask)])
        addresses.append(int(b_loc, 2))
    return addresses


def get_updates_simple(addr, value, mask):
    transformed = "".join(m if m != "X" else a for a, m in zip(addr, mask))
    return {addr: int(transformed, 2)}


def get_updates_complex(addr, value, mask):
    addr_masked = "".join(m if m == "1" else a for a, m in zip(addr, mask))
    return {a: int(value) for a in get_address_variations(addr_masked, mask)}


def solve(raw_in, get_updates_func):
    mem = {}
    for line in raw_in:
        cmd, value = line.split(" = ")
        if cmd == "mask":
            mask = value
        else:
            addr = parse_addr(cmd)
            updates = get_updates_func(addr, value, mask)
            mem.update(updates)
    return sum(v for v in mem.values())


if __name__ == "__main__":
    raw_in = read_input("inputs/day_14.txt")

    answer_1 = solve(raw_in, get_updates_simple)
    answer_2 = solve(raw_in, get_updates_complex)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
