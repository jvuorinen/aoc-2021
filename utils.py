import os
import requests


def print_answers(a1, a2, day):
    print(f"== Day {day} ==")
    print(a1)
    print(a2)
    print()


def _read(fp):
    # print(f"Reading {fp}")
    with open(fp) as fh:
        result = fh.read()
    return result


def read(year=None, day=None):
    if (year is None) or (day is None):
        return _read("inputs/tmp.txt")
    fp = f"inputs/{year}/day{day}.txt"
    if not os.path.exists(fp):
        load_data(year, day)
    return _read(fp)


def load_data(year, day):
    token = os.environ["SESSION_TOKEN"]
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token}
    )
    fp = f"inputs/{year}/day{day}.txt"
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    with open(fp, "w") as file:
        file.write(res.text[:-1])  # Remove last newline
    print(f"Downloaded and wrote data: {fp}")
