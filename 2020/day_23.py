from itertools import chain

from utils import read_input


class CircleNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedCircle:
    def __init__(self, values):
        self._set_values(values)

    def _set_values(self, iterable):
        _iter = iter(iterable)

        first_value = next(_iter)
        first_node = CircleNode(first_value)
        self.nodes = {first_value: first_node}
        self.cursor = first_node

        for i in _iter:
            node = CircleNode(i)
            self.nodes[i] = node
            self.cursor.next = node
            self.cursor = node

        self.nodes[i].next = first_node  # Wrap to circle
        self.cursor = first_node
        self.max_value = max(self.nodes)

    def peek(self, n):
        res = []
        node = self.cursor
        for _ in range(n):
            node = node.next
            res.append(node.value)
        return res

    def set_cursor(self, value):
        self.cursor = self.nodes[value]

    def __repr__(self):
        return f"LinkedCircle with {len(self.nodes)} nodes. Cursor is at {self.cursor}"


def move(circle, n):
    for _ in range(n):
        peek = circle.peek(4)
        picked_up, skip_to = peek[:3], peek[3]

        dst = circle.cursor.value - 1
        if dst == 0:
            dst = circle.max_value
        while dst in picked_up:
            dst -= 1
            if dst == 0:
                dst = circle.max_value

        # Remove the three
        circle.cursor.next = circle.nodes[skip_to]

        # Attach the picked up ones
        attach_point = circle.nodes[dst].next
        circle.nodes[dst].next = circle.nodes[picked_up[0]]
        circle.nodes[picked_up[2]].next = attach_point

        # Update cursor
        circle.cursor = circle.cursor.next


def solve_1(inputs):
    cups = LinkedCircle(inputs)
    move(cups, 100)

    cups.set_cursor(1)
    return "".join(str(i) for i in cups.peek(8))


def solve_2(inputs):
    MAX_VALUE = 1_000_000
    _inputs = chain(inputs, range(max(inputs) + 1, MAX_VALUE + 1))

    cups = LinkedCircle(_inputs)
    move(cups, 10_000_000)

    cups.set_cursor(1)
    a, b = cups.peek(2)
    return a * b


if __name__ == "__main__":
    raw_in = read_input("inputs/day_23.txt")
    inputs = [int(i) for i in raw_in[0]]

    answer_1 = solve_1(inputs)
    answer_2 = solve_2(inputs)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
