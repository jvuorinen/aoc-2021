import re
from utils import read, print_answers

def triang(n):
    return n*(n+1) // 2

y, x = map(int, re.findall(r"\d+", read(2015, 25)))

n = triang(x) + x * (y-1) + triang(y-2)
b, x, m = 20151125, 252533, 33554393

a1 = b * pow(x, n-1, m) % m
print_answers(a1, None, day=25)
