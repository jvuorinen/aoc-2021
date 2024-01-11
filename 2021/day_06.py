from utils import read_input

N_DAYS_PREGNANCY = 6
N_DAYS_CHILDHOOD = 8


def get_cleaned_input():
    raw_in = read_input("inputs/day_06.txt")
    dates = [int(i) for i in raw_in[0].split(",")]
    fishes = [0 for _ in range(N_DAYS_CHILDHOOD + 1)]

    for d in dates:
        fishes[d] += 1

    return fishes


def simulate_day(fishes):
    gen_size = fishes[0]
    nxt = fishes[1:] + [gen_size]  # newborns
    nxt[N_DAYS_PREGNANCY] += gen_size  # roll old ones
    return nxt


def solve(fishes, n_days):
    fishes = fishes.copy()

    for _ in range(n_days):
        fishes = simulate_day(fishes)

    return sum(fishes)


if __name__ == "__main__":
    fishes = get_cleaned_input()

    answer_1 = solve(fishes, 80)
    answer_2 = solve(fishes, 256)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
