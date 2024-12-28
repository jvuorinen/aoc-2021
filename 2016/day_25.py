from utils import print_answers


def test(a):
    num = a + 282 * 9
    res = []
    while num > 0:
        res.append(num % 2)
        num //= 2
    return len(res) % 2 == 0 and all([x == i % 2 for i, x in enumerate(res)])

a1 = next(n for n in range(1000) if test(n))
print_answers(a1, None, day=25)