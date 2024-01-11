from utils import read_input
import re


def parse_dict(user_chunk):
    items = user_chunk.split()
    tmp = [x.split(":") for x in items]
    d = {k: v for k, v in tmp}
    return d


def get_cleaned_input():
    tmp = read_input("inputs/day_04.txt", split_delimiter="\n\n")
    res = [parse_dict(x) for x in tmp]
    return res


def has_required_fields(d):
    REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    missing_keys = REQUIRED_KEYS - set(d)
    res = missing_keys == set()
    return res


def validate_fields(d):
    # First check schema
    SCHEMA = {
        "byr": r"^\d{4}$",
        "iyr": r"^\d{4}$",
        "eyr": r"^\d{4}$",
        "hgt": r"^\d+(cm|in)$",
        "hcl": r"^#([0-9]|[a-f]){6}$",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^\d{9}$",
        "cid": r".*",
    }

    schema_checks = [bool(re.search(SCHEMA[k], v)) for k, v in d.items()]

    if not all(schema_checks):
        return False

    # Then check specials
    hgt_val = int(d["hgt"][:-2])
    hgt_unit = d["hgt"][-2:]

    special_checks = [
        not (1920 <= int(d["byr"]) <= 2002),
        not (2010 <= int(d["iyr"]) <= 2020),
        not (2020 <= int(d["eyr"]) <= 2030),
        (hgt_unit == "cm") & (not (150 <= hgt_val <= 193)),
        (hgt_unit == "in") & (not (59 <= hgt_val <= 76)),
    ]

    if any(special_checks):
        return False
    else:
        return True


def drop_passports_with_missing_fields(dicts):
    have_all_fields = list(filter(has_required_fields, dicts))
    return have_all_fields


def drop_invalid_passports(dicts):
    have_all_fields = list(filter(has_required_fields, dicts))
    valids = list(filter(validate_fields, have_all_fields))
    return valids


if __name__ == "__main__":
    passports = get_cleaned_input()

    have_all_fields = drop_passports_with_missing_fields(passports)
    valid_passports = drop_invalid_passports(passports)

    print(f"Part 1 answer: {len(have_all_fields)}")
    print(f"Part 2 answer: {len(valid_passports)}")
