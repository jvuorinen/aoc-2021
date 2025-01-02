import numpy as np
import re
from utils import read, print_answers

A = np.zeros((1000, 1000), bool)
B = np.zeros((1000, 1000), int)

for line in read(2015, 6).split("\n"):
    a, b, c, d = map(int, re.findall(r'\d+',line))
    if "toggle" in line:
        A[a:c+1, b:d+1] = ~A[a:c+1, b:d+1]
        B[a:c+1, b:d+1] += 2
    else: 
        A[a:c+1, b:d+1] = ("on" in line)
        B[a:c+1, b:d+1] = (B[a:c+1, b:d+1] + (-1, 1)["on" in line]).clip(0)

print_answers(A.sum(), B.sum(), day=6)