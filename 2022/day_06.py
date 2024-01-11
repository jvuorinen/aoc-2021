from utils import read_file, print_answers


def solve(pkt, k):
    chunks = [pkt[i : i + k] for i in range(len(pkt) - k)]
    ns = [i for i, c in enumerate(chunks, k) if (len(set(c)) == k)]
    return ns[0]


if __name__ == "__main__":
    pkt = read_file("inputs/day_06b.txt")

    a1 = solve(pkt, 4)
    a2 = solve(pkt, 14)

    print_answers(a1, a2, day=6)
