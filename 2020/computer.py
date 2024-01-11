from utils import read_input


def _parse_instruction(s):
    a, b = s.split(" ")
    return a, int(b)


class Computer:
    def __init__(self):
        self.reset()

    def load_program(self, s):
        self.program = s

    def read_program_from_file(self, path):
        p = [_parse_instruction(x) for x in read_input(path)]
        self.load_program(p)

    def reset(self):
        self.pointer = 0
        self.acc = 0
        self.i = 0
        self.error_loop = False
        self.finished_successfully = False
        self.previous_states = set()

    def step(self):
        code, value = self.program[self.pointer]

        # Halt execution if state is not valid
        if self.finished_successfully == True:
            print("Already finished")
            return

        if self.error_loop == True:
            print("Cannot run in a loop state")
            return

        # Determine next state
        if code == "nop":
            pointer_next = self.pointer + 1
            acc_next = self.acc
        if code == "acc":
            pointer_next = self.pointer + 1
            acc_next = self.acc + value
        if code == "jmp":
            pointer_next = self.pointer + value
            acc_next = self.acc

        next_state = (pointer_next, acc_next)

        # Update state
        if pointer_next >= len(self.program):
            self.finished_successfully = True
            # print("Finished running successfully")
            return

        if pointer_next not in self.previous_states:
            self.pointer, self.acc = next_state
            self.previous_states.add(pointer_next)
            self.i += 1
            return
        else:
            self.error_loop = True
            # print(f"Loop found on iteration {self.i}, aborting")
            return

    def run(self):
        while (not self.error_loop) & (not self.finished_successfully):
            self.step()

    def __repr__(self):
        s = f"Computer with state:\n"
        s += f"  i {self.i}\n"
        s += f"  pointer {self.pointer}\n"
        s += f"  acc {str(self.acc)}\n"
        s += f"  error_loop {self.error_loop}\n"
        s += f"  finished_succesfully {self.finished_successfully}\n"
        s += f"Number of states visited: {len(self.previous_states)}\n"
        return s
