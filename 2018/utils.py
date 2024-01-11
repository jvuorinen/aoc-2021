def read(fp):
    with open(fp) as fh:
        result = fh.read()
    return result


def print_answers(a1, a2, day):
    print(f"== Day {day} ==")
    print(a1)
    print(a2)
    print()


def complex_to_tuple(c):
    return (int(c.real), int(c.imag))
