from utils import read_file, print_answers
import re
from dataclasses import dataclass
from math import prod
from copy import deepcopy
from typing import Union


class HugeNumber:
    def __init__(self, init=None, mods=None):
        if init is not None:
            self.mods = {x: init % x for x in mods}
        else:
            self.mods = mods

    def __repr__(self) -> str:
        return "<huge>"

    def __add__(self, k):
        new = {x: (old + k) % x for x, old in self.mods.items()}
        return HugeNumber(mods=new)

    def __mul__(self, k):
        if isinstance(k, int):
            new = {x: (old * k) % x for x, old in self.mods.items()}
        elif isinstance(k, HugeNumber):
            prods = [a * b for a, b in zip(self.mods.values(), k.mods.values())]
            new = {x: p % x for p, x in zip(prods, self.mods.keys())}
        return HugeNumber(mods=new)

    def __mod__(self, k):
        return self.mods[k]


@dataclass
class Monkey:
    id: int
    items: list[Union[int, HugeNumber]]
    op: str
    div: int
    targets: list[int]
    inspections: int = 0


def parse_monkey(s):
    get_nums = lambda s: [int(x) for x in re.findall("\d+", s)]

    ss = s.split("\n")
    return Monkey(
        id=get_nums(ss[0])[0],
        items=get_nums(ss[1].split(":")[1]),
        op=ss[2].split("= ")[1].replace("old", "x"),
        div=get_nums(ss[3])[0],
        targets=get_nums(ss[4] + ss[5]),
    )


def simulate(monkeys, rounds, manageable):
    monkeys = deepcopy(monkeys)

    if not manageable:
        mods = [m.div for m in monkeys]
        for m in monkeys:
            m.items = [HugeNumber(x, mods) for x in m.items]

    for _ in range(rounds):
        for m in monkeys:
            while m.items:
                m.inspections += 1
                x = m.items.pop(0)
                x = eval(m.op)
                if manageable:
                    x //= 3
                tgt = m.targets[x % m.div != 0]
                monkeys[tgt].items.append(x)
    return monkeys


def get_mbiz(monkeys):
    return prod(sorted([m.inspections for m in monkeys])[-2:])


if __name__ == "__main__":
    raw_in = read_file("inputs/day_11b.txt")
    monkeys = [parse_monkey(s) for s in raw_in.split("\n\n")]

    sim1 = simulate(monkeys, 20, manageable=True)
    sim2 = simulate(monkeys, 10_000, manageable=False)

    a1 = get_mbiz(sim1)
    a2 = get_mbiz(sim2)

    print_answers(a1, a2, day=11)
