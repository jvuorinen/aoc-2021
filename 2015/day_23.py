from utils import print_answers


def solve(a):
    b = 0
    while a != 1:
        b += 1
        if a % 2 == 0:
            a //= 2
        else:
            a *= 3
            a += 1
    return b


print_answers(solve(9663), solve(77671), day=23)
