from utils import print_answers, read

stream = read(2017, 9)

lvl = 0
n_groups = 0
n_garbage = 0
ignore = False
in_garbage = False
for c in stream:
    if ignore:
        ignore = False
        continue
    match c, in_garbage:
        case "{", False:
            lvl += 1
            n_groups += lvl
        case "}", False:
            lvl -= 1
        case "<", False:
            in_garbage = True
        case ">", True:
            in_garbage = False
        case "!", True:
            ignore = True
        case _, True:
            n_garbage += 1

print_answers(n_groups, n_garbage, day=9)
