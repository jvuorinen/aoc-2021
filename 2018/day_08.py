from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Any
from utils import read, print_answers


class Parts(Enum):
    HEADER = 0
    META = 1


@dataclass
class Packet:
    subs_left: int
    n_meta: int
    parent: Optional[Any] = None
    children: list[Any] = field(default_factory=list)
    meta: list[int] = field(default_factory=list)


def parse(code):
    expected = Parts.HEADER
    pkt = None
    while code:
        if expected == Parts.HEADER:
            s, m, *code = code
            pkt = Packet(s, m, parent=pkt)
            expected = Parts.HEADER if s > 0 else Parts.META

        elif expected == Parts.META:
            pkt.meta, code = code[: pkt.n_meta], code[pkt.n_meta :]
            if pkt.parent:
                pkt.parent.children.append(pkt)
                pkt = pkt.parent
                pkt.subs_left -= 1
                expected = Parts.HEADER if pkt.subs_left else Parts.META
            else:
                return pkt


def value_1(pkt):
    return sum(pkt.meta) + sum([value_1(c) for c in pkt.children])


def value_2(pkt):
    if not pkt.children:
        return sum(pkt.meta)
    else:
        existing = [m for m in pkt.meta if m <= len(pkt.children)]
        return sum([value_2(pkt.children[m - 1]) for m in existing])


code = [int(x) for x in read("inputs/day_08b.txt").split()]
root = parse(code)

a1 = value_1(root)
a2 = value_2(root)
print_answers(a1, a2, day=8)
