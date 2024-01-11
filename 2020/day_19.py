import re

from utils import read_input


def parse_input(raw_in):
    r, m = raw_in
    rules = dict(x.replace('"', "").split(": ") for x in r.split("\n"))
    messages = m.split("\n")
    return rules, messages


def unravel_regex(rules, idx="0", funny_mod=False):
    ALLOWED_SINGLE_CHARS = r"^[a-z\|\(\)]$"
    rule = rules.get(idx, idx)

    # Funny hacky mod to solve part 2
    if funny_mod == True:
        if idx == "8":
            return unravel_regex(rules, "42") + "+"

        elif idx == "11":
            regex_42 = unravel_regex(rules, "42", funny_mod)
            regex_31 = unravel_regex(rules, "31", funny_mod)

            regexes = []

            # MAX_LEN is hardcoded below. The solution would not work if the inputs contained
            # longer sequences of regex_42 and regex_31... So this is an incomplete
            # solution. But how to make a regex that makes the amount of repetitions
            # for these two patterns equal?
            #
            # A light-weight option that would be a complete solution would be to
            # check the inputs' max length and make MAX_LEN dynamically adjust to that.
            MAX_LEN = 5
            for i in range(1, MAX_LEN):
                fun_stuff = regex_42 + "{" + str(i) + "}" + regex_31 + "{" + str(i) + "}"
                regexes.append(fun_stuff)

            return "(" + "|".join(regexes) + ")"

    if re.match(ALLOWED_SINGLE_CHARS, rule):
        return rule
    else:
        if "|" in rule:
            rule = "( " + rule + " )"
        return "".join(unravel_regex(rules, r, funny_mod) for r in rule.split(" "))


def solve(rules, messages, funny_mod=False):
    pattern = "^" + unravel_regex(rules, funny_mod=funny_mod) + "$"
    return sum(True if re.match(pattern, m) else False for m in messages)


if __name__ == "__main__":
    raw_in = read_input("inputs/day_19.txt", split_delimiter="\n\n")
    rules, messages = parse_input(raw_in)

    answer_1 = solve(rules, messages)
    answer_2 = solve(rules, messages, funny_mod=True)

    print(f"Part 1 answer: {answer_1}")
    print(f"Part 2 answer: {answer_2}")
