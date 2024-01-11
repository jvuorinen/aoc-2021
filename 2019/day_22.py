from utils import read_input

commands = read_input("inputs/day_22.txt")

D = 119315717514047
N = 101741582076661


def modinv(p, d):
    return pow(p, d - 2, d)


def reverse_deal(i):
    return D - 1 - i


def reverse_cut(i, c):
    return (i + c + D) % D


def reverse_increment(i, c):
    return modinv(c, D) * i % D


def f(x):
    for c in commands[::-1]:
        words = c.split()
        if c.startswith("cut"):
            x = reverse_cut(x, int(words[-1]))
        elif c.startswith("deal with"):
            x = reverse_increment(x, int(words[-1]))
        else:
            x = reverse_deal(x)
    return x % D


x = 2020
y = f(x)
z = f(y)
a = (y - z) * modinv(x - y, D) % D
b = (y - a * x) % D

a2 = int((pow(a, N, D) * x + (pow(a, N, D) - 1) * modinv(a - 1, D) * b) % D)
print(a2)
