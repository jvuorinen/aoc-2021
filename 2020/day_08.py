from computer import Computer


def generate_possible_variations(program):
    nop_idxes = [i for i, c in enumerate(program) if c[0] == "nop"]
    jmp_idxes = [i for i, c in enumerate(program) if c[0] == "jmp"]

    for ni in nop_idxes:
        p = program.copy()
        p[ni] = ("jmp", p[ni][1])
        yield p

    for ji in jmp_idxes:
        p = program.copy()
        p[ji] = ("nop", p[ji][1])
        yield p


def beat_it_until_it_works(computer):
    code_variations = generate_possible_variations(computer.program)

    while True:
        code_trial = next(code_variations)

        computer.reset()
        computer.load_program(code_trial)
        computer.run()

        if computer.finished_successfully:
            break


if __name__ == "__main__":
    computer = Computer()
    computer.read_program_from_file("inputs/day_08.txt")

    # Part 1
    computer.run()
    print(f"Part 1 answer: {computer.acc}")

    # Part 2
    beat_it_until_it_works(computer)
    print(f"Part 2 answer: {computer.acc}")
