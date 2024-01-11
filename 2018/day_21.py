from utils import print_answers


def get_test_order():
    r1 = r2 = r5 = 0

    tested = []
    while True:
        r2 = r1 | 65536
        r1 = 7902108
        while True:
            r5 = r2 % 256
            r1 = ((r1 + r5) * 65899) % 16777216
            if r2 < 256:
                # r5 = 0
                if r1 in tested:
                    return tested
                tested.append(r1)
                break
            r2 = r5 = r2 // 256


tested = get_test_order()

a1 = tested[0]
a2 = tested[-1]
print_answers(a1, a2, day=21)  # 6483199 13338900
