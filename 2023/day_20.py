from dataclasses import dataclass, field
from math import lcm
from utils import read_file, print_answers


@dataclass
class Pulse:
    type: int
    sender: str
    receiver: str

    def __str__(self):
        return f"{self.sender} ({self.type}) {self.receiver}"


@dataclass
class Flipflop:
    name: str
    targets: list[str]
    state: int = 0

    def process(self, p: Pulse):
        if p.type == 0:
            self.state ^= 1
            return [Pulse(self.state, self.name, tgt) for tgt in self.targets]
        else:
            return []


@dataclass
class Conjunction:
    name: str
    targets: list[str]
    mem: dict = field(default_factory=dict)

    def process(self, p: Pulse):
        self.mem[p.sender] = p.type
        type = 0 if all(self.mem.values()) else 1
        return [Pulse(type, self.name, tgt) for tgt in self.targets]


@dataclass
class Broadcaster:
    name: str
    targets: list[str]
    state = 0

    def process(self, p: Pulse):
        return [Pulse(p.type, self.name, tgt) for tgt in self.targets]


def parse(raw_in):
    data = [line.split(" -> ") for line in raw_in.split("\n")]
    network = {}

    for fr, tgts in data:
        tgts = tgts.split(", ")
        if fr == "broadcaster":
            network[fr] = Broadcaster(fr, tgts)
        else:
            type, name = fr[0], fr[1:]
            if type == "%":
                network[name] = Flipflop(name, tgts)
            elif type == "&":
                network[name] = Conjunction(name, tgts)

    for m in network.values():
        for t in m.targets:
            if isinstance(cj := network.get(t), Conjunction):
                cj.mem[m.name] = 0
    return network


def push_button(network, i, bookkeep):
    queue = [Pulse(0, "button", "broadcaster")]
    while queue:
        p = queue.pop(0)
        if p.receiver == "zh" and p.type == 1:
            bookkeep["zh_is_one"].append(i)
        if i <= 1000 and p.type == 1:
            bookkeep["n_high"] += 1
        if i <= 1000 and p.type == 0:
            bookkeep["n_low"] += 1
        if p.receiver in network:
            queue.extend(network[p.receiver].process(p))


if __name__ == "__main__":
    raw_in = read_file("inputs/day_20b.txt")
    network = parse(raw_in)

    bookkeep = {"n_high": 0, "n_low": 0, "zh_is_one": []}
    for i in range(1, 4000):
        push_button(network, i, bookkeep)

    a1 = bookkeep["n_high"] * bookkeep["n_low"]
    a2 = lcm(*bookkeep["zh_is_one"])
    print_answers(a1, a2, day=20)  # Correct: 839775244, 207787533680413
