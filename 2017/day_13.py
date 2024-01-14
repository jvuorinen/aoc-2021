from utils import read, print_answers

raw = read(2017, 13).split("\n")
fwall = [tuple(map(int, line.split(": "))) for line in raw]

# Part 1
a1 = sum([d * r * (d % (r * 2 - 2) == 0) for d, r in fwall])


# Part 2
def get_delay(fwall):
    for delay in range(10_000_000):
        for d, r in fwall:
            if (d + delay) % (r * 2 - 2) == 0:
                break
        else:
            return delay


print_answers(a1, get_delay(fwall), day=13)  # 2688 3876272
