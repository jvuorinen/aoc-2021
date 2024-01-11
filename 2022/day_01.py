from utils import read_file, print_answers

if __name__ == "__main__":
    raw_in = read_file("inputs/day_01.txt").split("\n\n")
    sums = sorted([sum(map(int, x.split())) for x in raw_in])[::-1]

    print_answers(sums[0], sum(sums[:3]), day=1)
